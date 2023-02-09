from selenium.webdriver.common.by import By


settings_button = (By.CLASS_NAME, "color-settings")
small_page = (By.CSS_SELECTOR, 'div[class="Tabs_tabsContainer__+lLBt"]')
participants_button = (By.XPATH, '//span[text()="Participants"]')
email_field = (By.CSS_SELECTOR, 'input[placeholder="E-mail"]')
select_access_level = (By.XPATH, '//div[@class="Grid_col__NSAHt Grid_span_12__pZfWv Grid_span_up_lg_4__qvPjP"]/select')
invite_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-settings"]')
error_message = (By.CSS_SELECTOR, 'div[class="Alert_content__04oih"]')
invited_filed = (By.XPATH, '//i[text()="Invited"]')
access_level = (By.CSS_SELECTOR, 'select[style="width: 100%;"]')
projects_button = (By.XPATH, '//span[text()="Projects"]')
add_project = (By.CSS_SELECTOR, 'button[class="btn-filter color-settings"]')
name_project = (By.CSS_SELECTOR, 'input[name="name"]')
save_button = (By.CSS_SELECTOR, 'button[class="btn _inp-size4 color-settings"]')
edit_button = (By.CSS_SELECTOR, '.Icon_root__qRNSV')
setting_open = (By.CSS_SELECTOR, 'div[class="rc-dialog-content"]')
team_button = (By.XPATH, '//span[text()="Team"]')
team_name = (By.CSS_SELECTOR, 'input[value]')
main_currency = (By.CSS_SELECTOR, 'input[placeholder="Select currency"]')
month_start = (By.XPATH, '//option[text()="Floating month"]')
week_start = (By.XPATH, '//option[text()="Use default"]')
time_zone = (By.CSS_SELECTOR, 'input[class="select-search__input"]')
select_save_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-success"]')
delete_team = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-danger"]')
key_button = (By.CSS_SELECTOR, 'svg[class="Icon_root__qRNSV"]')
deny_account = (By.CSS_SELECTOR, '.Button_button__QS2NC')
button_save = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn color-success"]')
analytics_details = (By.XPATH, '//*[@id="popup-container_1"]/main/div[2]/div[3]/div[2]/a')
restricted_user = (By.CSS_SELECTOR, 'input[name="user-c0a5c4d9-f4fc-4f04-bbf7-263f7a79bd01-role"]')
