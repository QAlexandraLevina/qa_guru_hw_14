from selene import browser, be, have
import time

### НЕСТАБИЛЬНЫЕ ШАГИ С РЕДИРЕКТАМИ ###
class FooterWithRedirect:
    def __init__(self):
        self.top_footer_logo = browser.element(".footer-top__logo")
        self.top_footer_small_logo = browser.element(".footer-top__small-logo")
        self.disclaimer = browser.element(".disclaimer")
        self.bottom_footer_info = browser.element(".info")
        self.bottom_footer_payments = browser.element(".payment-methods")
        self.vkontakte_link = browser.element("li a[href='https://vk.com/rpbaze']")
        self.telegram_link = browser.element("li a[href='https://t.me/bazerp")
        self.discord_link = browser.element("li a[href='https://discord.com/channels/470680918408036362/1148223367078490162")
        self.youtube_link = browser.element("li a[href='https://www.youtube.com/@Baze_RP")
        self.user_agreement_link = browser.element("a[href='/user-agreement']")
        self.privacy_policy_link = browser.element("a[href='/privacy-policy']")
        self.project_rules_link = browser.element(".links__list li:nth-child(3) .links__item") # НЕТ ССЫЛКИ В HTML


    """Клик по сайтам и страницам"""
    def click_vkontakte_link(self):
        self.vkontakte_link.click()
        return self


    def click_telegram_link(self):
        self.telegram_link.click()
        return self


    def click_discord_link(self):
        self.discord_link.click()
        return self


    def click_youtube_link(self):
        self.youtube_link.click()
        return self


    def click_user_agreement_link(self):
        self.user_agreement_link.click()
        return self


    def click_privacy_policy_link(self):
        self.privacy_policy_link.click()
        return self


    """Закрытие вкладок и возврат на первоначальную позицию"""
    def close_tab_and_back(self):
        browser.close_current_tab()
        window_tabs = browser.config.driver.window_handles
        browser.config.driver.switch_to.window(window_tabs[0])
        return self


    """Проверка редиректа на сайты и страницы"""
    def should_redirect_to_vkontakte(self):
        time.sleep(5)
        browser.should(have.tabs_number_greater_than(1))
        window_tabs = browser.config.driver.window_handles
        browser.config.driver.switch_to.window(window_tabs[-1])
        browser.should(have.url_containing("vk.com"))
        return self


    def should_redirect_to_telegram(self):
        time.sleep(5)
        browser.should(have.tabs_number_greater_than(1))
        window_tabs = browser.config.driver.window_handles
        browser.config.driver.switch_to.window(window_tabs[-1])
        browser.should(have.url_containing("t.me"))
        return self

    def should_redirect_to_discord(self):
        browser.should(have.tabs_number_greater_than(1))
        window_tabs = browser.config.driver.window_handles
        browser.config.driver.switch_to.window(window_tabs[-1])
        browser.should(have.url_containing("discord.com"))
        return self

    def should_redirect_to_youtube(self):
        browser.should(have.tabs_number_greater_than(1))
        window_tabs = browser.config.driver.window_handles
        browser.config.driver.switch_to.window(window_tabs[-1])
        browser.should(have.url_containing("youtube.com"))
        return self

    def should_redirect_to_user_agreement_page(self):
        browser.should(have.tabs_number_greater_than(1))
        window_tabs = browser.config.driver.window_handles
        browser.config.driver.switch_to.window(window_tabs[-1])
        browser.should(have.url_containing("/user-agreement"))
        return self

    def should_redirect_to_privacy_policy_page(self):
        browser.should(have.tabs_number_greater_than(1))
        window_tabs = browser.config.driver.window_handles
        browser.config.driver.switch_to.window(window_tabs[-1])
        browser.should(have.url_containing("/privacy-policy"))
        return self


    """Проверка отображения ссылок и их текста"""
    def should_display_correct_links(self):
        self.vkontakte_link.should(be.visible).should(have.text("VKONTAKTE"))
        self.telegram_link.should(be.visible).should(have.text("TELEGRAM"))
        self.discord_link.should(be.visible).should(have.text("DISCORD"))
        self.youtube_link.should(be.visible).should(have.text("YOUTUBE"))
        self.user_agreement_link.should(be.visible).should(have.text("ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"))
        self.privacy_policy_link.should(be.visible).should(have.text("ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ"))
        self.project_rules_link.should(be.visible).should(have.text("ПРАВИЛА ПРОЕКТА"))
        return self


    """Проверка отображения текста"""
    def should_display_texts_footer(self):
        self.top_footer_logo.should(be.visible)
        self.top_footer_small_logo.should(be.visible).should(have.text("BAZE © 2025"))
        ex_text = ("BAZE RP НЕ СВЯЗАНА, НЕ СПОНСИРУЕТСЯ И НЕ ПОДДЕРЖИВАЕТСЯ КОМПАНИЕЙ TAKE-TWO INTERACTIVE SOFTWARE, INC. (ROCKSTAR GAMES). "
                   "ВСЕ ИСПОЛЬЗУЕМЫЕ ТОРГОВЫЕ МАРКИ И ДРУГИЕ ПРЕДМЕТЫ ИНТЕЛЛЕКТУАЛЬНОЙ СОБСТВЕННОСТИ ЯВЛЯЮТСЯ СОБСТВЕННОСТЬЮ СООТВЕТСТВУЮЩИХ ВЛАДЕЛЬЦЕВ.")
        self.disclaimer.should(be.visible).should(have.exact_text(ex_text))
        self.bottom_footer_info.should(be.visible).should(have.text('ООО "EDUCATION STUDIO'))
        self.bottom_footer_info.should(be.visible).should(have.text('ИНН 311 619 091'))
        self.bottom_footer_info.should(be.visible).should(have.text('BARHAYOT MFY, 12 MAVZESI , 20А-UY'))
        self.bottom_footer_payments.should(be.visible)
        return self