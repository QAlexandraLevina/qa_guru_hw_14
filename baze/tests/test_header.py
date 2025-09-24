import allure

from baze.pages.authorization_form import AuthorizationForm
from baze.pages.header import Header


@allure.feature('Test Case #1: Проверка хедера у неавторизованного пользователя')
def test_header_unauthorized_user(setup_browser, open_base_page):
    # browser = setup_browser

    allure.title("Проверка элементов хедера и переход по каждой вкладке")
    header = Header()

    with allure.step("Проверка отображения элементов хедера неавторизованным пользователем"):
        header.should_have_menu_items_unauthorized()

    with allure.step("Прокликивание элементов хедера неавторизованным пользователем"):
        header.click_all_tabs_header_unauthorized()


@allure.feature('Test Case #2: Проверка хедера у авторизованного пользователя')
def test_header_authorized_user(setup_browser, authenticated_user):
    # browser = setup_browser

    allure.title("Проверка авторизованного пользователя")
    header = Header()
    auth_form = AuthorizationForm()


    auth_form.should_authorized_profile()

    allure.title("Проверка элементов хедера и переход по каждой вкладке")
    with allure.step("Проверка отображения элементов хедера авторизованным пользователем"):
        header.should_have_menu_items_authorized(authenticated_user)

    with allure.step("Прокликивание элементов хедера авторизованным пользователем"):
        header.click_all_tabs_header_authorized(authenticated_user)