from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from locators import locators_balance as loc


class BalancePage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        log_in = LoginPage(self.driver)
        log_in.open_login_page()
        log_in.enter_correct_email(correct_email="ele67900@gmail.com")
        log_in.enter_correct_password(correct_password="12345678ABC_")
        log_in.click_next()

    def open_balance_page(self):
        self.find(loc.balance_button).click()

    def select_current_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.balance_button))
        return self.find(loc.type_accounts).text

    def click_edit_button(self):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(loc.edit_button)).click()
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(loc.credit_card)).click()
        self.find(loc.cash).click()

    def select_new_type_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.cash)).click()

    def select_save_button(self):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(loc.save_button)).click()

    def click_amount_button(self):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(loc.amount_button)).click()

    def enter_amount_money(self, money):
        self.find(loc.amount_money).send_keys(money).send_keys(Keys.ENTER)

    def get_error_messsage(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.error_message))
        return self.find(loc.error_message).text

    def choose_user(self, user):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.user_button)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.enter_user)).\
            send_keys(user).send_keys(Keys.ENTER)

    def choose_project(self, project):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.project_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.enter_project)).\
            send_keys(project).send_keys(Keys.ENTER)

    def user_sort(self):
        user = self.find(loc.sort_user_box)
        return user.is_enabled()

    def project_sort(self):
        project = self.find(loc.sort_project_box)
        return project.is_enabled()
