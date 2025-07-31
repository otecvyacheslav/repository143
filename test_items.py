from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_this_course(browser, request):
    browser.get(link)

    find_need_element = browser.find_element(By.CSS_SELECTOR, ".hidden-xs > strong")
    text_find_need_element = find_need_element.text
    assert (
        text_find_need_element == "Total carrito:"
    ), "Нет этих слов, вероятно не тот язык"


# Total carrito:
