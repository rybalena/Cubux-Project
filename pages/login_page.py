from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators_login as loc
import time


class LoginPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://new.cubux.net/login'

    def open_login_page(self):
        self.open()

    def enter_incorrect_email(self, incorrect_email):
        self.find(loc.field_email).send_keys(incorrect_email)

    def enter_correct_email(self, correct_email):
        self.find(loc.field_email).send_keys(correct_email)

    def enter_incorrect_password(self, incorrect_password):
        self.find(loc.field_password).send_keys(incorrect_password)

    def enter_correct_password(self, correct_password):
        self.find(loc.field_password).send_keys(correct_password)

    def enter_new_password(self, new_password):
        self.find(loc.field_password).send_keys(new_password)

    def click_next(self):
        self.find(loc.enter_button).click()

    def check_error_message(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.error_message))
        return self.find(loc.error_message).text

    def check_analytics_diagram(self):
        diagram = self.find(loc.analytics_diagram)
        return diagram.is_enabled()

    def logout(self):
        self.find(loc.menu_bar).click()
        self.find(loc.log_out_button).click()

    def languages_panel(self):
        panel = self.find(loc.language_panel)
        return panel.is_enabled()

    def login_recover(self, email):
        self.find(loc.login_recover).click()
        self.find(loc.email_incorrect).send_keys(email)
        time.sleep(3)

    def click_recaptcha(self):
        recapture_box = self.find(loc.recaptcha).click()
        ActionChains(self.driver).click(recapture_box).send_keys(Keys.ENTER).perform()
        time.sleep(10)

    def click_send_instruction_buttton(self):
        self.find(loc.send_instruction_button).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.error_message_2)).text
