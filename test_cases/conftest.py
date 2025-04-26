import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):  # this method  required browser name taken or providing command line input
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser chrome or edge")


@pytest.fixture()  # this fixture return the value of browser which pass in setup fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):  # after value received,that browser instance was created and return it.
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("unsupported browser")
    return driver


# For pytest html report ##############
# hook for Adding environmental info in html report ##############
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce project -nopcommerce '
    config.stash[metadata_key]['Module'] = 'Admin Login test'
    config.stash[metadata_key]['Tester'] = 'Yogesh'

# hook for delete/modify environmental info in html report ##############
# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
