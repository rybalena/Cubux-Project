from pages.budget_page import BudgetPage
import allure


@allure.feature("Budget")
@allure.story("Check the diagram by month in the pop-up window")
def test_pop_up_window(driver):
    budget = BudgetPage(driver)
    with allure.step("Open page"):
        budget.open_page()
    with allure.step("Open budget page"):
        budget.open_budget_page()
    with allure.step("Clear the checkboxes for Monthly and Food."):
        budget.clear_fields()
    with allure.step("Observe pop-up window for month February with diagram and budget"):
        assert budget.pop_up_window_appear() is True


@allure.feature("Budget")
@allure.story("Add new table budget")
def test_new_table_budget(driver):
    budget = BudgetPage(driver)
    with allure.step("Open page"):
        budget.open_page()
    with allure.step("Open budget page"):
        budget.open_budget_page()
    with allure.step("Select add button"):
        budget.select_add_button()
    with allure.step("Enter name"):
        budget.enter_name(name='budget')
    with allure.step("Click next"):
        budget.click_next()
    with allure.step("Able to see the budget table"):
        assert budget.budget_table() is True


@allure.feature("Budget")
@allure.story("After enter the value, the data is no longer 0.00 in the cell")
def test_value(driver):
    budget = BudgetPage(driver)
    with allure.step("Open page"):
        budget.open_page()
    with allure.step("Open budget page"):
        budget.open_budget_page()
    with allure.step("Open budget table"):
        budget.open_budget_table()
    with allure.step("Select edit table"):
        budget.select_edit_table()
    with allure.step("Enter data"):
        budget.add_data(data='1234')
    with allure.step("Check value not equal to 0"):
        value = budget.back_value()
        assert value != "0.00"
