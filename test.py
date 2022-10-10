import search_google
from selenium import webdriver


SEARCH_TEXT = "Think24.ru"
BAD_SEARCH_TEXT = "e;kghrke;jvb;kjvb/kvb'vbqe'vbqekjvbq;kfjbqekvjc"
SEARCH_TITLE = "Think24.ru - Поиск в Google"
LINK_NAME = "Think24 App"
TARGET_URL = "https://think24.ru/"

if __name__ == "__main__":
    print("not implemented, please call with pytest \n \"python3 -m pytest -v  test.py\"")
    exit(0)

driver = webdriver.Chrome()
Page = search_google.GoogleSearch(driver)

def test1_open_google():
    Page.go_to_site()
    assert Page.check_title("Google")
    assert Page.check_url("https://www.google.com/")

def test2_search_in_google():
    Page.search_word(SEARCH_TEXT)
    assert Page.result_stats

def test3_find_link_in_search_result():
    Page.search_result_by_name(LINK_NAME)
    assert Page.check_title(SEARCH_TITLE)


def test4_click_on_search_result():
    Page.click_on_search_result(name=LINK_NAME)
    assert Page.check_title(LINK_NAME)
    assert Page.check_url(TARGET_URL)

def test_teardown():
    driver.close()


