import pytest

def pytest_addoption(parser):
    parser.addoption("--remote", action="store")

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

