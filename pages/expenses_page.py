from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators_expenses as loc


class ExpensesPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        log_in = LoginPage(self.driver)
        log_in.open_login_page()
        log_in.enter_correct_email(correct_email="ele67900@gmail.com")
        log_in.enter_correct_password(correct_password="12345678ABC_")
        log_in.click_next()

    def open_expenses_page(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(loc.expenses_button)).click()

    def select_user_account(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.select_user_account))

    def delete_button(self):
        self.window_scroll()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.delete_button)).click()

    def alert_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.alert_message)).text

    def select_create_copy(self):
        WebDriverWait(self.driver, 10).until_not(EC.element_to_be_selected(loc.select_create_copy)).click()

    def select_ok_button(self):
        WebDriverWait(self.driver, 10).until_not(EC.element_to_be_selected(loc.ok_button)).click()

    def select_all_time(self):
        WebDriverWait(self.driver, 10).until_not(EC.element_to_be_selected(loc.select_all_time)).click()

    def pop_up_window_appear(self):
        popup = self.find(loc.pop_up_window)
        return popup.is_enabled()

    def select_date_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.date_button)).click()

    def choose_dates(self, date, date2):
        self.window_scroll()
        self.find(loc.date).send_keys(date)
        self.find(loc.date_2).send_keys(date2)

    def table_appear_with_expenses(self):
        table = self.find(loc.table_appear)
        return table.is_enabled()
