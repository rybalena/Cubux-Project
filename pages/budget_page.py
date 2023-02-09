from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators_budget as loc


class BudgetPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        log_in = LoginPage(self.driver)
        log_in.open_login_page()
        log_in.enter_correct_email(correct_email="ele67900@gmail.com")
        log_in.enter_correct_password(correct_password="12345678ABC_")
        log_in.click_next()

    def open_budget_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.budget_button)).click()

    def clear_fields(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.food_checkbox)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.monthly_checkbox)).click()

    def pop_up_window_appear(self):
        diagram = self.find(loc.pop_up_window)
        return diagram.is_enabled()

    def select_add_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.add_table)).click()

    def enter_name(self, name):
        self.find(loc.enter_name).send_keys(name)

    def click_next(self):
        self.find(loc.next_button).click()

    def budget_table(self):
        table = self.find(loc.budget_table)
        return table.is_enabled()

    def open_budget_table(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.open_table)).click()

    def select_edit_table(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.edit_table)).click()

    def back_value(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.value)).text

    def add_data(self, data):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.enter_data)).send_keys(data)
