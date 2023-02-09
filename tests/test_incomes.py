from pages.incomes_page import IncomesPage
import allure


@allure.feature("Incomes")
@allure.story("Select the green button without enter any data")
def test_green_button(driver):
    incomes = IncomesPage(driver)
    with allure.step("Open page"):
        incomes.open_page()
    with allure.step("Open Incomes page"):
        incomes.open_incomes_page()
    with allure.step("Select Add incomes button"):
        incomes.select_incomes_button()
    with allure.step("Select + button"):
        incomes.select_plus_button()
    with allure.step("Observe the message"):
        message = incomes.observe_message()
        assert message == "Select an account"


@allure.feature("Incomes")
@allure.story("Sort incomes by amount of money")
def test_sort_incomes(driver):
    incomes = IncomesPage(driver)
    with allure.step("Open page"):
        incomes.open_page()
    with allure.step("Open Incomes page"):
        incomes.open_incomes_page()
    with allure.step("Select Amount button"):
        incomes.select_amount_button()
    with allure.step("Enter the amount of money"):
        incomes.enter_amount_money(amount='89')
    with allure.step("Observe the message"):
        message_2 = incomes.observe_message_2()
        assert message_2 == "There no transactions"


@allure.feature("Incomes")
@allure.story("Changing salary amount after add salary")
def test_change_incomes(driver):
    incomes = IncomesPage(driver)
    with allure.step("Open page"):
        incomes.open_page()
    with allure.step("Open Incomes page"):
        incomes.open_incomes_page()
    with allure.step("Add salary"):
        incomes.add_salary(dates='2/8/2023', salary='3456')
    with allure.step("Observe summary salary in diagram block"):
        assert incomes.observe_salary_diagram_change() is True
