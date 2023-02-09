from pages.login_page import LoginPage
import allure


@allure.feature("Log in")
@allure.story("Log in with incorrect email and password")
def test_incorrect_login(driver):
    log_in = LoginPage(driver)
    with allure.step("Open log in page"):
        log_in.open_login_page()
    with allure.step("Enter incorrect email"):
        log_in.enter_incorrect_email(incorrect_email="email@mail.com")
    with allure.step("Enter incorrect password"):
        log_in.enter_incorrect_password(incorrect_password="123940_4")
    with allure.step("Click enter"):
        log_in.click_next()
    with allure.step("Able to see error message"):
        message = log_in.check_error_message()
        assert message == "Incorrect username or password"


@allure.feature("Log in")
@allure.story("Log in with correct email and password")
def test_correct_login(driver):
    log_in = LoginPage(driver)
    with allure.step("Open log in page"):
        log_in.open_login_page()
    with allure.step("Enter email"):
        log_in.enter_correct_email(correct_email="ele67900@gmail.com")
    with allure.step("Enter password"):
        log_in.enter_correct_password(correct_password="12345678ABC_")
    with allure.step("Click enter"):
        log_in.click_next()
    with allure.step("Able to see the Analytics diagram"):
        assert log_in.check_analytics_diagram()


@allure.feature("Log in")
@allure.story("Forgot password")
def test_forgot_password(driver):
    log_in = LoginPage(driver)
    with allure.step("Open log in page"):
        log_in.open_login_page()
    with allure.step("Enter email"):
        log_in.enter_correct_email(correct_email="ele67900@gmail.com")
    with allure.step("Click Forgot password?"):
        log_in.login_recover(email="thatha@gmail.com")
    with allure.step("Click recaptcha checkbox"):
        log_in.click_recaptcha()
    with allure.step("Click send instruction"):
        log_in.click_send_instruction_buttton()
    with allure.step("Observe error message"):
        message_2 = log_in.get_error_message()
        assert message_2 == "There is no user with such E-mail"
