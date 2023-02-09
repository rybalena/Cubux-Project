from pages.balance_page import BalancePage
import allure


@allure.feature("Balance")
@allure.story("Change account type from Card to Cash")
def test_change_type_account(driver):
    balance = BalancePage(driver)
    with allure.step("Open page"):
        balance.open_page()
    with allure.step("Open balance page"):
        balance.open_balance_page()
    with allure.step("Select the current card account type"):
        card_account = balance.select_current_account()
    with allure.step("Select edit button"):
        balance.click_edit_button()
    with allure.step("Change account type to cash account"):
        balance.select_new_type_account()
    with allure.step("Enter save button"):
        balance.select_save_button()
        cash_account = balance.select_current_account()
        assert card_account == 'Card' and cash_account == 'Cash'


@allure.feature("Balance")
@allure.story("Enter minus the amount of money in transactions")
def test_minus_amount_money(driver):
    balance = BalancePage(driver)
    with allure.step("Open page"):
        balance.open_page()
    with allure.step("Open balance page"):
        balance.open_balance_page()
    with allure.step("Click on the amount button"):
        balance.click_amount_button()
    with allure.step("Enter the amount of money"):
        balance.enter_amount_money(money='-444444')
    with allure.step("Able to see error message"):
        message = balance.get_error_messsage()
        assert message == "Unconfirmed transactions"


@allure.feature("Balance")
@allure.story("Sort balance by User and Project")
def test_sort_balance(driver):
    balance = BalancePage(driver)
    with allure.step("Open page"):
        balance.open_page()
    with allure.step("Open balance page"):
        balance.open_balance_page()
    with allure.step("Choose User"):
        balance.choose_user(user='Elena Rybina')
    with allure.step("Choose Project"):
        balance.choose_project(project='Budget 2020')
    with allure.step("Able to see sort by User"):
        assert balance.user_sort() is True
    with allure.step("Able to see sort by Project"):
        assert balance.project_sort() is True
