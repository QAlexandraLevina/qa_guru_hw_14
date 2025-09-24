import allure
from baze.pages_unstable.start_game_with_redirect import StartGameWithRedirect


### НЕСТАБИЛЬНЫЕ ТЕСТЫ С РЕДИРЕКТАМИ ###
def test_start_game_with_redirect(setup_browser, open_base_page):
    # browser = setup_browser


    """Инициализация экземпляра класса StartGame"""
    start_game_with_redirect = StartGameWithRedirect()


    """Выполнение шагов и проверок"""
    with allure.step("Нажатие на кнопку 'Начать игру'"):
        start_game_with_redirect.click_button_play_game()


    with allure.step("Проверка отображения заголовка раздела 'Как начать играть' и названий всех вкладок"):
        start_game_with_redirect.should_display_heading_and_name_tabs_in_how_start_game()


    with allure.step("Проверка вкладки 'Покупка игры'"):
        start_game_with_redirect.should_display_subtitle_and_description_pay_game_tab()


    with allure.step("Редирект в Steam, проверка редиректа и возвращение на сайт BAZE RP"):
        start_game_with_redirect.click_steam_link().should_link_to_steam().close_tab_and_back()


    with allure.step("Редирект в Epic Games, проверка редиректа и возвращение на сайт BAZE RP"):
        start_game_with_redirect.click_epic_games_link().should_link_to_epic_games().close_tab_and_back()


    with allure.step("Редирект в Rockstar Games, проверка редиректа и возвращение на сайт BAZE RP"):
        start_game_with_redirect.click_rockstar_games_link().should_link_to_rockstar_games().close_tab_and_back()


    with allure.step("Переключение на вкладку 'Установка лаунчера'"):
        start_game_with_redirect.click_launcher_installation_tab()


    with allure.step("Проверка вкладки 'Установка лаунчера'"):
        start_game_with_redirect.should_display_subtitle_and_description_launcher_installation_tab()


    with allure.step("Редирект на установку Rage MP, проверка редиректа и возвращение на сайт BAZE RP"):
        start_game_with_redirect.click_rage_mp_link().should_link_to_rage_mp().close_tab_and_back()


    with allure.step("Переключение на вкладку 'Подключение'"):
        start_game_with_redirect.click_connection_tab()


    with allure.step("Проверка вкладки 'Подключение'"):
        start_game_with_redirect.should_display_subtitle_and_description_connection_tab()


    with allure.step("Возвращение на вкладку 'Покупка игры'"):
        start_game_with_redirect.click_pay_game_tab()