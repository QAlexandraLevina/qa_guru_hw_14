import allure
from baze.pages.start_game import StartGame


def test_start_game(setup_browser, open_base_page):
    # browser = setup_browser

    """Инициализация экземпляра класса StartGame"""
    start_game = StartGame()


    allure.title("Проверка блока 'Как начать играть' при нажатии на кнопку 'Начать игру'")
    with allure.step("Нажатие на кнопку 'Начать игру'"):
        start_game.click_button_play_game()


    with allure.step("Проверка отображения заголовка раздела 'Как начать играть' и названий всех вкладок"):
        start_game.should_display_heading_and_name_tabs_in_how_start_game()


    with allure.step("Проверка вкладки 'Покупка игры'"):
        start_game.should_display_subtitle_and_description_pay_game_tab()


    with allure.step("Проверка отображения и кликабельности ссылки в Steam"):
        start_game.should_link_to_steam()


    with allure.step("Проверка отображения и кликабельности ссылки в Epic Games"):
        start_game.should_link_to_epic_games()


    with allure.step("Проверка отображения и кликабельности ссылки в Rockstar Games"):
        start_game.should_link_to_rockstar_games()


    with allure.step("Переключение на вкладку 'Установка лаунчера'"):
        start_game.click_launcher_installation_tab()


    with allure.step("Проверка вкладки 'Установка лаунчера'"):
        start_game.should_display_subtitle_and_description_launcher_installation_tab()


    with allure.step("Проверка отображения и кликабельности ссылки на установку Rage MP"):
        start_game.should_link_to_rage_mp()


    with allure.step("Переключение на вкладку 'Подключение'"):
        start_game.click_connection_tab()


    with allure.step("Проверка вкладки 'Подключение'"):
        start_game.should_display_subtitle_and_description_connection_tab()


    with allure.step("Возвращение на вкладку 'Покупка игры'"):
        start_game.click_pay_game_tab()