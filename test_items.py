from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)
    assert (
        browser.find_element(By.CSS_SELECTOR, ".add-to-basket > button[value]"),
    ), "Нет такой кнопки"
