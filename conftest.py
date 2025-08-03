import pytest  # импорт пайтеста
from selenium import webdriver  # импорт вебдрайвера
from selenium.webdriver.chrome.options import (Options)
# импорт работы с настройками селениума
import time  # импорт времени


def pytest_addoption(parser):  # парсер
    # Парсер - это программа или скрипт, который автоматизированно извлекает и структурирует данные с веб-сайтов. Процесс извлечения данных называется парсингом. Парсеры находят и извлекают нужную информацию из HTML-кода страницы, преобразуя ее в удобный для пользователя формат
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose your language: ru, en, ec, fr",
    )


@pytest.fixture(
    scope="function"
)  # фикстура, задается правило, что отдельный запуск тест-браузера для каждой функции
def browser(request):  # реквест (гугли, не объяснить правильно в 2-х словах)
    user_language = request.config.getoption(
        "--language"
    )  # переменная = запрос настроек языка
    options = Options()  # переменная = настройки, которые мы импортировали из селениум
    options.add_experimental_option(
        "prefs", {"intl.accept_language": user_language}
    )  # Как раз те самые настройки, просто прикрепили к отдельной переменной, можно было в скобки посадить....берем работу с языком
    print("\nstart browser..")  # вывод в консоль, что начался запуск браузера
    options.add_argument(
        f"--lang={user_language}"
    )  # взяли переменную и добавили (т.к. некоторые версии Chrome и ChromeDriver лучше реагируют на `–lang` на системном уровне, который передается как аргумент командной строки.)
    browser = webdriver.Chrome(options=options)  # запускаем хром
    browser.implicitly_wait(10)  # добавили неявное ожидание до 10 секунд
    if user_language == "fr":  # если используем фр
        print("\nuse french language..")  # принт в консоль
    elif user_language == "es":  # если используем ес
        print("\nuse spanish language..")  # принт в консоль
    else:  # иначе
        raise pytest.UsageError(
            "--language should be 'fr' or 'es'"
        )  # выпадет ошибка с описанием в скобках
    yield browser  # Значение выражения yield* само по себе равно последнему значению итерируемого объекта (т.е., того когда done равно true). То есть в конце передаем в browser то, что ниже
    time.sleep(10)  # ожидание в 10 секунд
    print("\nclose browser..")  # принт в консоль
    browser.quit()  # закрытие браузера
