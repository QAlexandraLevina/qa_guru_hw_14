import os
import allure
import pytest
from selene.support.shared import browser
from baze.pages.authorization_form import AuthorizationForm
from baze.data.users import UserData
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from baze.utils import attachments
from dotenv import load_dotenv


DEFAULT_BROWSER_VERSION = "128.0"

"""Настройка параметров для браузера"""
def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )


"""Загрузка переменных сред из файла .env"""
@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


"""Получение информации о значении параметра browser из командной строки"""
@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION


    """Настройка драйвера"""
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)


    """Создание переменных, cсылающихся на секретные данные"""
    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASSWORD')


    """Создание драйвера"""
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )


    """Передача драйвера в Selene"""
    browser.config.driver = driver


    """Настройка параметров браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 30
    browser.config.base_url = "https://bazerp.com"


    yield browser


    """Добавление аттачей после теста"""
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_html(browser)
    attachments.add_video(browser)


    """Закрытие браузера"""
    browser.quit()


"""Авторизация для проверки функционала у авторизованного пользователя"""
@pytest.fixture
def user_authorized():
    return UserData(
        "alexandralevina@gmail.com",
        "Password123."
    )

@allure.step("Открытие главной страницы в браузере")
def open_base_page_step():
    browser.open("/")

@pytest.fixture(scope='function')
def open_base_page(setup_browser):
    open_base_page_step()

    yield

@pytest.fixture(scope='function')
def authenticated_user(setup_browser, open_base_page, user_authorized):
    authenticated_form = AuthorizationForm()
    authenticated_form.authorization_user(user_authorized)

    yield user_authorized