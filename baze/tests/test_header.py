import allure

from baze.pages.authorization_form import AuthorizationForm
from baze.pages.header import Header


def test_header_unauthorized_user(setup_browser, open_base_page):
    # browser = setup_browser

    """Инициализация экземпляра класса Header"""
    header = Header()

    with allure.step("Проверка отображения элементов хедера неавторизованным пользователем"):
        header.should_have_menu_items_unauthorized()

    with allure.step("Прокликивание элементов хедера неавторизованным пользователем"):
        header.click_all_tabs_header_unauthorized()


def test_header_authorized_user(setup_browser, authenticated_user):
    # browser = setup_browser

    """Инициализация экземпляра класса Header"""
    header = Header()

    """Проверка того, что пользователь авторизовался"""
    AuthorizationForm.should_authorized_profile(authenticated_user)

    with allure.step("Проверка отображения элементов хедера авторизованным пользователем"):
        header.should_have_menu_items_authorized(authenticated_user)

    with allure.step("Прокликивание элементов хедера авторизованным пользователем"):
        header.click_all_tabs_header_authorized(authenticated_user)