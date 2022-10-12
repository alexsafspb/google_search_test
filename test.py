import search_google
from selenium import webdriver
import pytest

if __name__ == "__main__":
    print("not implemented, please call with pytest \n \"python3 -m pytest -v  test.py\"")
    exit(0)

class TestGoogleSearch:
    test_data = {}
    def test_setup(self,remote):
        if remote:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)
        else:
           driver = webdriver.Chrome()
        self.test_data["Page"] = search_google.GoogleSearch(driver)

    def test1_open_google(self):
        Page = self.test_data["Page"]
        Page.go_to_site()
        assert Page.check_title("Google")
        assert Page.check_url("https://www.google.com/")

    def test2_search_in_google(self,search_text):
        Page = self.test_data["Page"]
        Page.search_word(search_text)
        assert Page.result_stats

    def test3_find_link_in_search_result(self, link_name, search_title):
        Page = self.test_data["Page"]
        Page.search_result_by_name(link_name)
        assert Page.check_title(search_title)

    def test4_click_on_search_result(self, link_name, target_url):
        Page = self.test_data["Page"]
        Page.click_on_search_result(name=link_name)
        assert Page.check_title(link_name)
        assert Page.check_url(target_url)

    def test_teardown(self):
        Page = self.test_data["Page"]
        Page.driver.quit()


