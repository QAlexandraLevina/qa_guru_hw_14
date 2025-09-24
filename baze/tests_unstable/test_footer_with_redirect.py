import allure
from baze.pages_unstable.footer_with_redirect import FooterWithRedirect

### НЕСТАБИЛЬНЫЕ ТЕСТЫ С РЕДИРЕКТАМИ ###
def test_footer_with_redirect(setup_browser, open_base_page):
    browser = setup_browser

    """Инициализация экземпляра класса Footer"""
    footer_with_redirect = FooterWithRedirect()


    """Выполнение шагов и проверок"""
    with allure.step("Скролл до футера"):
        browser.execute_script("arguments[0].scrollIntoView();", footer_with_redirect.bottom_footer_info.locate())


    with allure.step("Проверка отображения ссылок и их текста"):
       footer_with_redirect.should_display_correct_links()


    with allure.step("Проверка отображения текста"):
       footer_with_redirect.should_display_texts_footer()


    with allure.step("Редирект на VKONTAKTE, проверка редиректа и возвращение на сайт BAZE RP"):
       footer_with_redirect.click_vkontakte_link().should_link_to_vkontakte().close_tab_and_back()


    with allure.step("Редирект на TELEGRAM, проверка редиректа и возвращение на сайт BAZE RP"):
       footer_with_redirect.click_telegram_link().should_link_to_telegram().close_tab_and_back()


    with allure.step("Редирект в DISCORD, проверка редиректа и возвращение на сайт BAZE RP"):
       footer_with_redirect.click_discord_link().should_link_to_discord().close_tab_and_back()


    with allure.step("Редирект на YOUTUBE, проверка редиректа и возвращение на сайт BAZE RP"):
       footer_with_redirect.click_youtube_link().should_link_to_youtube().close_tab_and_back()


    with allure.step("Редирект на ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ, проверка редиректа и возвращение к футеру на главной странице"):
       footer_with_redirect.click_user_agreement_link().should_link_to_user_agreement_page().close_tab_and_back()


    with allure.step("Редирект на ПОЛИТИКУ КОНФИДЕНЦИЛЬНОСТИ, проверка редиректа и возвращение к футеру на главной странице"):
       footer_with_redirect.click_privacy_policy_link().should_link_to_privacy_policy_page().close_tab_and_back()