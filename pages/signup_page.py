from selenium.common import NoSuchElementException
from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators_signup as loc
import random
import string
import time


class SignupPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_signup_page(self):
        self.open()
        self.window_scroll()
        self.click_signup_page()

    def enter_name(self):
        letters = string.ascii_letters
        name = "".join(random.sample(letters, 10))
        self.find(loc.field_name).send_keys(name)

    def enter_second_name(self):
        letters = string.ascii_letters
        name = "".join(random.sample(letters, 10))
        self.find(loc.second_name).send_keys(name)

    def enter_new_email(self, email):
        self.find(loc.register_field_email).send_keys(email)

    def enter_new_password(self, password):
        self.window_scroll()
        self.find(loc.register_field_password).send_keys(password)

    def enter_country(self, country):
        country_field = self.find(loc.field_country)
        ActionChains(self.driver).click(country_field).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).\
            send_keys(country).send_keys(Keys.ENTER).perform()
        time.sleep(6)

    def checkbox_country(self):
        country = self.find(loc.field_country)
        return country.is_enabled()

    def click_recaptcha(self):
        recapture_box = self.find(loc.recaptcha)
        ActionChains(self.driver).click(recapture_box).send_keys(Keys.ENTER).perform()
        time.sleep(10)

    def check_button_register(self):
        WebDriverWait(self.driver, 5).until_not(EC.element_attribute_to_include(loc.submit_button, "disabled"))
        check_button = self.find(loc.submit_button)
        return check_button.is_enabled()

    def enter_submit_button(self):
        WebDriverWait(self.driver, 5).until_not(EC.element_attribute_to_include(loc.submit_button, "disabled"))
        self.find(loc.submit_button).click()

    def submit_button(self):
        self.find(loc.submit_button).click()

    def check_account_delete(self):
        self.find(loc.menu_bar).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.small_page))
        self.find(loc.delete_button).click()
        self.find(loc.current_password).send_keys('BKVVyyyydfdsde__745!_!')
        self.find(loc.reasons_for_deletion).send_keys('N/A N/A N/A N/A N/A')
        self.find(loc.delete_profile_button).click()
        page_url = self.driver.current_url
        return "https://new.cubux.net/login" in page_url

    def checkbox_balance(self):
        try:
            self.find(loc.checkbox_balance).is_enabled()
        except NoSuchElementException:
            return True
        else:
            return False

    def balance_button(self):
        balance = self.find(loc.balance_button)
        return balance.is_enabled()

    def disable_settings(self):
        try:
            self.find(loc.checkbox_balance).is_enabled()
        except NoSuchElementException:
            return True
        else:
            return False

    def fail_signup(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.fail_signup_message)).text
