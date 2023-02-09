from selenium.webdriver.common.by import By


balance_button = (By.CSS_SELECTOR, 'a[class="btn-icon _size2 color-balance"]')
type_accounts = (By.XPATH, '//td[text()="Card"]')
edit_button = (By.CSS_SELECTOR, 'button[title="Edit"]')
credit_card = (By.CSS_SELECTOR, 'span[class="hex-icon-symbol"]')
cash = (By.CSS_SELECTOR, 'div[class="hex-btn"]')
save_button = (By.CSS_SELECTOR, 'button[class="btn _inp-size4 color-income"]')
small_page = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]')
amount_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ ButtonDropdown_button__spRKX"]')
amount_money = (By.XPATH, '//*[@id="popup-container_1"]/main/div[3]/table/tbody/tr[1]/td[4]/div/div/div/div[2]/'
                          'form/input')
error_message = (By.XPATH, '//span[text()="Unconfirmed transactions"]')
user_button = (By.XPATH, '//button[text()="User"]')
enter_user = (By.XPATH, '//*[@id="popup-container_1"]/main/div[4]/table/tbody/tr[1]/td[6]'
                        '/div/div/div/div[2]/select')
project_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ ButtonDropdown_button__spRKX"]')
enter_project = (By.CSS_SELECTOR, 'input[class="select-search__input"]')
sort_user_box = (By.XPATH, '//span[[text()="User"]')
sort_project_box = (By.XPATH, '//span[text()="Project"]')
