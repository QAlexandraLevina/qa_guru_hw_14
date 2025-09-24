import allure
from baze.pages.authorization_form import AuthorizationForm


def test_authorization_form(setup_browser, open_base_page, user_authorized):
    # browser = setup_browser
    """Инициализация экземпляров класса AuthorizationForm"""
    authorization_form = AuthorizationForm()

    allure.title("Авторизация и проверка авторизации пользователя")
    with allure.step("Авторизация пользователя"):
        authorization_form.authorization_user(user_authorized)

    with allure.step("Проверка авторизованного пользователя"):
        authorization_form.should_authorized_profile()