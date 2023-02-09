from selenium.webdriver.common.by import By


expenses_button = (By.CSS_SELECTOR, 'a[class="btn-icon _size2 color-expense"]')
select_user_account = (By.XPATH, '//*[@id="popup-container_1"]/main/div[3]/div[2]/div[6]/div/table/tbody/tr[2]/td[6]')
delete_button = (By.CSS_SELECTOR, 'svg[class="Icon_root__qRNSV"]')
alert_message = (By.XPATH, '//div[text()="Are you sure to delete the transaction? This action cannot be undone."]')
select_create_copy = (By.CSS_SELECTOR, 'button[title="Create a copy"]')
ok_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-expense"]')
select_all_time = (By.CSS_SELECTOR, 'a[href="/team/295171/expense/details?since=&until="]')
pop_up_window = (By.XPATH, '//*[@id="popup-container_1"]/main/div[3]/div[2]/div[3]/div[1]/div/div[2]')
date_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ ButtonDropdown_button__spRKX"]')
date = (By.CSS_SELECTOR, 'input[class="_inp-size4 input-icon icon-calendar react-datepicker-ignore-onclickoutside"]')
date_2 = (By.CSS_SELECTOR, 'input[class="_inp-size4 input-icon icon-calendar"]')
table_appear = (By.CSS_SELECTOR, 'table[class="list-category TransactionsTable_root__ehmR3 '
                                'TransactionsTable__withFilter__Gf4CV"]')
