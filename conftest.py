import pytest
# import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose your language: ru, en, ec, fr",
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_language": user_language})
    print("\nstart browser..")
    browser = webdriver.Chrome(options=options)
    # browser.implicitly_wait(10)
    if user_language == "ru":
        print("\nuse russian language..")
    elif user_language == "es":
        print("\nuse espanian language..")
    else:
        raise pytest.UsageError("--language should be 'es'")
    yield browser
    time.sleep(10)
    print("\nclose browser..")
    browser.quit()
