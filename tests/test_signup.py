from pages.signup_page import SignupPage
import allure


@allure.feature("Sign up")
@allure.story("Submit button disabled until all data has been enter")
def test_signup_button(driver):
    signup = SignupPage(driver)
    with allure.step("Open Sign up page"):
        signup.open_signup_page()
    with allure.step("Select name"):
        signup.enter_name()
    with allure.step("Select second name"):
        signup.enter_second_name()
    with allure.step("Enter email"):
        signup.enter_new_email(email="rgsghsgehjyj@gmail.com")
    with allure.step("Enter password"):
        signup.enter_new_password(password="12345678ABC_")
    with allure.step("Enter country"):
        signup.enter_country(country="Albania")
    with allure.step("Check that submit button is disabled"):
        assert signup.check_button_register() is True


@allure.feature("Sign up")
@allure.story("Submit button disabled until all data has been enter")
def test_fields(driver):
    signup = SignupPage(driver)
    with allure.step("Open Sign up page"):
        signup.open_signup_page()
    with allure.step("Select name"):
        signup.enter_name()
    with allure.step("Select second name"):
        signup.enter_second_name()
    with allure.step("Check that field country is enabled"):
        assert signup.checkbox_country() is True
    with allure.step("Check that field balance is disabled"):
        assert signup.checkbox_balance() is False


@allure.feature("Sign up")
@allure.story("Failed to sign up with already created account")
def test_already_created_account(driver):
    signup = SignupPage(driver)
    with allure.step("Open Sign up page"):
        signup.open_signup_page()
    with allure.step("Select name"):
        signup.enter_name()
    with allure.step("Select second name"):
        signup.enter_second_name()
    with allure.step("Enter email"):
        signup.enter_new_email(email="ele67900@gmail.com")
    with allure.step("Enter password"):
        signup.enter_new_password(password="12345678ABC_")
    with allure.step("Enter country"):
        signup.enter_country(country='Albania')
    with allure.step("Select recaptcha checkbox"):
        signup.click_recaptcha()
    with allure.step("Enter submit button"):
        signup.submit_button()
    with allure.step("Able to see error message"):
        message = signup.fail_signup()
        assert message == 'E-mail "ele67900@gmail.com" has already been taken.'


@allure.feature("Sign up")
@allure.story("Create account")
def test_sign_up(driver):
    signup = SignupPage(driver)
    with allure.step("Open Sign up page"):
        signup.open_signup_page()
    with allure.step("Select name"):
        signup.enter_name()
    with allure.step("Select second name"):
        signup.enter_second_name()
    with allure.step("Enter email"):
        signup.enter_new_email(email="messkji@gmail.com")
    with allure.step("Enter password"):
        signup.enter_new_password(password="dfbhrHKQemm_33_!_jj_")
    with allure.step("Enter country"):
        signup.enter_country(country='Albania')
    with allure.step("Select recaptcha checkbox "):
        signup.click_recaptcha()
    with allure.step("Enter submit button"):
        signup.submit_button()
    with allure.step("Able to see the balance on the page"):
        assert signup.balance_button()


@allure.feature("Sign up")
@allure.story("Delete account")
def test_delete_account(driver):
    signup = SignupPage(driver)
    with allure.step("Open Sign up page"):
        signup.open_signup_page()
    with allure.step("Select name"):
        signup.enter_name()
    with allure.step("Select second name"):
        signup.enter_second_name()
    with allure.step("Enter email"):
        signup.enter_new_email(email="agagjkme3399007@gmail.com")
    with allure.step("Enter password"):
        signup.enter_new_password(password="BKVVyyyydfdsde__745!_!")
    with allure.step("Enter country"):
        signup.enter_country(country="Albania")
    with allure.step("Select recaptcha checkbox"):
        signup.click_recaptcha()
    with allure.step("Enter submit button"):
        signup.enter_submit_button()
    with allure.step("Delete account"):
        signup.check_account_delete()
    with allure.step("Make sure settings menu bar is disable"):
        assert signup.disable_settings() is True
