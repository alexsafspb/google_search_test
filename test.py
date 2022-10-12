import search_google
from selenium import webdriver
import pytest

if __name__ == "__main__":
    print("not implemented, please call with pytest \n \"python3 -m pytest -v  test.py\"")
    exit(0)

@pytest.mark.usefixtures("oneTimeSetUp")
class TestGoogleSearchi():

    def test1_open_google(self):
        self.Page.go_to_site()
        assert self.Page.check_title("Google")
        assert self.Page.check_url("https://www.google.com/")

    def test2_search_in_google(self,search_text):
        self.Page.search_word(search_text)
        assert self.Page.result_stats

    def test3_find_link_in_search_result(self, link_name, search_title):
        self.Page.search_result_by_name(link_name)
        assert self.Page.check_title(search_title)

    def test4_click_on_search_result(self, link_name, target_url):
        self.Page.click_on_search_result(name=link_name)
        assert self.Page.check_title(link_name)
        assert self.Page.check_url(target_url)



