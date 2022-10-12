import pytest

def pytest_addoption(parser):
    parser.addoption("--remote", action="store")

@pytest.fixture()
def search_text():
    SEARCH_TEXT = "Think24.ru"
    return SEARCH_TEXT

@pytest.fixture()
def search_title():
    SEARCH_TITLE = "Think24.ru - Поиск в Google"
    return SEARCH_TITLE

@pytest.fixture()
def link_name():
    LINK_NAME = "Think24 App"
    return LINK_NAME

@pytest.fixture()
def target_url():
    TARGET_URL = "https://think24.ru/"
    return TARGET_URL

#@pytest.fixture(scope='session')
#def remote(request):
#    name_value = request.config.option.remote
#    if name_value is None:
#        pytest.skip()

def pytest_addoption(parser):
    parser.addoption(
        "--remote", action="store_true", default=False, help="use remote selenium webdriver"
    )


@pytest.fixture
def remote(request):
    return request.config.getoption("--remote")

