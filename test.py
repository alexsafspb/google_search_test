import search_google
from selenium import webdriver
import time

SEARCH_TEXT = "Think24.ru"
BAD_SEARCH_TEXT = "e;kghrke;jvb;kjvb/kvb'vbqe'vbqekjvbq;kfjbqekvjc"
SEARCH_TITLE = "Think24.ru - Поиск в Google"
LINK_NAME = "Think24 App"

driver = webdriver.Chrome()
Page = search_google.GoogleSearch(driver)

def test1_open_google():
    Page.go_to_site()
    assert Page.driver.title == "Google"

def test2_search_in_google():
    Page.search_word(SEARCH_TEXT)
    assert Page.result_stats

def test3_find_in_search_result():
    Page.search_result_by_name(LINK_NAME)
    assert Page.driver.title == SEARCH_TITLE

def test4_click_on_search_result():
    Page.click_on_search_result(name=LINK_NAME)
    assert Page.driver.title == LINK_NAME


def test_teardown():
    driver.close()

if __name__ == "__main__":

    test1_open_google()
    test2_search_in_google()
    test3_find_in_search_result()
    test4_click_on_search_result()
    time.sleep(1)
    test_teardown()