from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators_settings as loc


class SettingsPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        log_in = LoginPage(self.driver)
        log_in.open_login_page()
        log_in.enter_correct_email(correct_email="ele67900@gmail.com")
        log_in.enter_correct_password(correct_password="12345678ABC_")
        log_in.click_next()

    def click_settings_button(self):
        self.find(loc.settings_button).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(loc.small_page))

    def click_participants_button(self):
        self.find(loc.participants_button).click()

    def enter_email_field(self, email):
        self.find(loc.email_field).send_keys(email)

    def select_access_level(self):
        self.find(loc.select_access_level).send_keys('administrator')

    def click_invite_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc.invite_button)).click()

    def get_error_message(self):
        return self.find(loc.error_message).text

    def invitation_field(self):
        invited = self.find(loc.invited_filed)
        return invited.is_enabled()

    def access_level(self):
        access = self.find(loc.access_level)
        return access.is_enabled()

    def click_projects_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc.projects_button)).click()

    def add_project(self):
        self.find(loc.add_project).click()

    def add_name_project(self, name):
        self.find(loc.add_project).send_keys(name)

    def click_save_button(self):
        self.find(loc.save_button).click()

    def edit_project_button(self):
        edit = self.find(loc.edit_button)
        return edit.is_enabled()

    def click_team_button(self):
        self.find(loc.team_button).click()

    def enter_team_name(self, name):
        self.find(loc.team_name).send_keys(name)

    def select_main_currency(self):
        self.find(loc.main_currency).send_keys('USD')

    def select_month_start(self):
        self.find(loc.month_start).send_keys('2')

    def select_week_start(self):
        self.find(loc.week_start).send_keys('1')

    def select_time_zone(self):
        self.find(loc.time_zone).send_keys('America')

    def select_save_button(self):
        self.find(loc.select_save_button).click()

    def delete_team(self):
        delete = self.find(loc.delete_team)
        return delete.is_enabled()

    def click_key_button(self):
        self.find(loc.key_button).click()

    def change_restricted_user(self):
        self.find(loc.restricted_user).click()

    def select_deny_account(self):
        self.find(loc.deny_account).click()

    def button_save(self):
        self.find(loc.button_save).click()

    def check_analytics_details(self):
        details = self.find(loc.analytics_details)
        return details.is_enabled()
