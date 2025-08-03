from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)

    find_need_element = browser.find_element(
        By.CSS_SELECTOR, ".add-to-basket > button[value]"
    )
    text_find_need_element = find_need_element.text
    print(f"find {text_find_need_element}")
    assert (
        text_find_need_element == "Ajouter au panier"
        or text_find_need_element == "Añadir al carrito"
    ), "Нет этих слов, вероятно не тот язык"
