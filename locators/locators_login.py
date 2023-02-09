from selenium.webdriver.common.by import By


field_email = (By.ID, "loginform-username")
field_password = (By.ID, "loginform-password")
enter_button = (By.CSS_SELECTOR, 'button[class="login100-form-btn button-loading"]')
error_message = (By.XPATH, '//div[text()="Incorrect username or password"]')
analytics_diagram = (By.ID, 'google_esf')
menu_bar = (By.CSS_SELECTOR, 'svg[xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" class="Icon_root__qRNSV"]')
log_out_button = (By.XPATH, '//button[text()="Logout"]')
language_panel = (By.CSS_SELECTOR, 'ul[class="languages-flag-menu"]')
login_recover = (By.CSS_SELECTOR, 'a[href="/login/recover"]')
email_incorrect = (By.ID, 'recoverform-mail')
recaptcha = (By.XPATH, '//*[@id="recoverform-verifycode_captcha"]/div/div/iframe')
send_instruction_button = (By.CSS_SELECTOR, 'button[class="login100-form-btn"]')
error_message_2 = (By.XPATH, '//*[@id="w0"]/div[1]/div')
