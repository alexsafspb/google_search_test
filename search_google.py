#Google search helper
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://google.com"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def check_title(self, title="Google", time=10):
        return WebDriverWait(self.driver, time).until(EC.title_contains(title),
                                                      message=f"Can't find title \"{title}\"")
class GoogleSearchError(Exception):
    pass

class GoogleSearchLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.NAME, "q")
    LOCATOR_GOOGLE_SEARCH_RESULTS = (By.ID, "search")
    LOCATOR_GOOGLE_SEARCH_RESULTS_STAT = (By.ID, "result-stats")

class GoogleSearch(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_result = None
        self.search_element = None
        self.result_stats = None

    def check_search_results(self,stat_text):
        SEARCH_FAILED_RU = "Результатов: примерно 0 "
        SEARCH_FAILED_EN = "About 0 results "
        result_stats = stat_text.split("(")[0]
        if (result_stats == SEARCH_FAILED_RU) or (result_stats == SEARCH_FAILED_EN):
            return False
        else:
            return True

    def search_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.send_keys(word + "\n")
        self.check_title(word)
        result_stats = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_RESULTS_STAT)
        self.result_stats = self.check_search_results(result_stats.text)
        self.search_result = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_RESULTS)
        return self.search_result

    def search_result_by_name(self, name):
        locator_search_results = (By.XPATH, '//h3[ text()="' + name + '"]')
        if self.result_stats:
            self.search_element = self.find_elements(locator_search_results)[0]
            return self.search_element
        else:
            raise GoogleSearchError("No search results")

    def click_on_search_result(self, search_element=None, name=""):
        if self.result_stats:
            if not search_element:
                search_element = self.search_element
            search_element.click()
            self.check_title(name)
        else:
            raise GoogleSearchError("No search results")

if __name__ == "__main__":
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    #options.add_argument('--lang=en_US')
    #driver = webdriver.Chrome(options=options)
    # options doesn't work.
    # no ideas how to change LANGUAGE variable to en_US
    driver = webdriver.Chrome()
    Page = GoogleSearch(driver)
    Page.go_to_site()
    print(Page.check_title())
    search = Page.search_word("Think24.ru")
    print(search.text)
    element = Page.search_result_by_name("Think24 App")
    Page.click_on_search_result(element, "Think24 App")
    time.sleep(1)
    driver.close()