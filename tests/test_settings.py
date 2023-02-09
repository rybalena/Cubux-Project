from pages.settings_page import SettingsPage
import allure


@allure.feature("Settings")
@allure.story("Invite a new user on the participants page")
def test_invitation(driver):
    settings = SettingsPage(driver)
    with allure.step("Open page"):
        settings.open_page()
    with allure.step("Click settings button"):
        settings.click_settings_button()
    with allure.step("Open participants page"):
        settings.click_participants_button()
    with allure.step("Enter participant email"):
        settings.enter_email_field(email='holahola7733@gmail.com')
    with allure.step("Choose access level"):
        settings.select_access_level()
    with allure.step("Click invite button"):
        settings.click_invite_button()
    with allure.step("Able to see 'Invited' next to the participant email"):
        assert settings.invitation_field()


@allure.feature("Settings")
@allure.story("Create a new project on the projects tab")
def test_create_new_project(driver):
    settings = SettingsPage(driver)
    with allure.step("Open page"):
        settings.open_page()
    with allure.step("Click settings button"):
        settings.click_settings_button()
    with allure.step("Open projects page"):
        settings.click_projects_button()
    with allure.step("Click on the Add project button"):
        settings.add_project()
    with allure.step("Enter the name of the new project"):
        settings.add_name_project(name='Budget 2023')
    with allure.step("Click save button"):
        settings.click_save_button()
    with allure.step("Able to edit the project"):
        assert settings.edit_project_button()


@allure.feature("Settings")
@allure.story("Create a new team on the team page")
def test_create_team(driver):
    settings = SettingsPage(driver)
    with allure.step("Open page"):
        settings.open_page()
    with allure.step("Click settings button"):
        settings.click_settings_button()
    with allure.step("Open team page"):
        settings.click_team_button()
    with allure.step("Enter team name"):
        settings.enter_team_name(name='Dragon team')
    with allure.step("Select main currency"):
        settings.select_main_currency()
    with allure.step("Select month start"):
        settings.select_month_start()
    with allure.step("Select week start"):
        settings.select_week_start()
    with allure.step("Select time zone"):
        settings.select_time_zone()
    with allure.step("Click save button"):
        settings.select_save_button()
    with allure.step("Able to Delete the team"):
        assert settings.delete_team()
