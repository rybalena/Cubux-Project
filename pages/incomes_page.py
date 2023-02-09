from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators_incomes as loc


class IncomesPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        log_in = LoginPage(self.driver)
        log_in.open_login_page()
        log_in.enter_correct_email(correct_email="ele67900@gmail.com")
        log_in.enter_correct_password(correct_password="12345678ABC_")
        log_in.click_next()

    def open_incomes_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.incomes_page)).click()

    def select_incomes_button(self):
        self.find(loc.add_incomes_button).click()

    def select_plus_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.select_plus_button)).click()

    def observe_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.observe_message)).text

    def select_amount_button(self):
        self.window_scroll()
        self.find(loc.amount_button).click()

    def enter_amount_money(self, amount):
        self.find(loc.enter_amount).send_keys(amount).click()

    def observe_message_2(self):
        return self.find(loc.observe_message_2).text

    def add_salary(self, dates, salary):
        self.find(loc.add_incomes_button).click()
        self.find(loc.select_account).click()
        self.find(loc.select_cash).click()
        self.find(loc.select_category).click()
        self.find(loc.select_salary).click()
        self.find(loc.select_date).send_keys(dates)
        self.find(loc.add_money).send_keys(salary)
        self.find(loc.ok_button).click()

    def observe_salary_diagram_change(self):
        return self.find(loc.diagram_block).is_enabled()
