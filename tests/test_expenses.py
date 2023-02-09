from pages.expenses_page import ExpensesPage
import allure


@allure.feature("Expenses")
@allure.story("Delete expenses transaction")
def test_delete_transaction(driver):
    expenses = ExpensesPage(driver)
    with allure.step("Open page"):
        expenses.open_page()
    with allure.step("Open Expenses page"):
        expenses.open_expenses_page()
    with allure.step("Select user account"):
        expenses.select_user_account()
    with allure.step("Select Delete button"):
        expenses.delete_button()
    with allure.step("Able to see a warning message"):
        message = expenses.alert_message()
        assert message == "Are you sure to delete the transaction? This action cannot be undone."


@allure.feature("Expenses")
@allure.story("Check the pop up window with expenses for All time")
def test_transaction_pop_up_window(driver):
    expenses = ExpensesPage(driver)
    with allure.step("Open page"):
        expenses.open_page()
    with allure.step("Open Expenses page"):
        expenses.open_expenses_page()
    with allure.step("Select Create a copy transaction"):
        expenses.select_create_copy()
    with allure.step("Select Ok button"):
        expenses.select_ok_button()
    with allure.step("Select All time button expenses"):
        expenses.select_all_time()
    with allure.step("Select a time period on the diagram and observe pop up window with expanses"):
        assert expenses.pop_up_window_appear() is True


@allure.feature("Expenses")
@allure.story("Sort expenses by date")
def test_sort_expenses(driver):
    expenses = ExpensesPage(driver)
    with allure.step("Open page"):
        expenses.open_page()
    with allure.step("Open Expenses page"):
        expenses.open_expenses_page()
    with allure.step("Select Date button"):
        expenses.select_date_button()
    with allure.step("Choose dates"):
        expenses.choose_dates(date='2/5/2023', date2='2/8/2023')
    with allure.step("Observe the table with sort expenses by date"):
        assert expenses.table_appear_with_expenses() is True
