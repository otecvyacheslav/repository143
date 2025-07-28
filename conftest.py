import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

@pytest.fixture(scope="function")
def browser():
    print("\nоткрытие браузера для теста..")
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nзакрытие браузера..")
    browser.quit()