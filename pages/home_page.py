from pages.base_page import BasePage
from selenium.webdriver.common.by import By

signup_page = (By.CSS_SELECTOR, 'a[href="/login/register"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://new.cubux.net/login'

    def open(self):
        self.driver.get(self.page_url)

    def click_signup_page(self):
        self.find(signup_page).click()
