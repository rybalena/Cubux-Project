from selenium.webdriver.common.by import By


incomes_page = (By.CSS_SELECTOR, 'a[class="btn-icon _size2 color-income"]')
add_incomes_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ icon _size1 _extra-space color-income"]')
select_plus_button = (By.CSS_SELECTOR, 'button[title="Save and create one more"]')
observe_message = (By.XPATH, '//div[text()="Select an account"]')
amount_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ ButtonDropdown_button__spRKX"]')
enter_amount = (By.XPATH, '//*[@id="popup-container_1"]/main/div[3]/div[2]/div[6]/div/table/'
                          'tbody/tr[1]/td[3]/div/div/div/div[2]/form/input')
observe_message_2 = (By.XPATH, 'td[text()="There are no transactions"]')
select_account = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/button[1]')
select_cash = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button[2]')
select_category = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/button[2]')
select_salary = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/button[2]')
select_date = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ hex-center react-datepicker-ignore-onclickoutside"]')
add_money = (By.CSS_SELECTOR, 'input[class="currency"]')
ok_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-income"]')
diagram_block = (By.XPATH, '//*[@id="popup-container_1"]/main/div[3]/div[2]/div[5]/div[1]/'
                           'div/div/svg/g[2]/text[12]')
