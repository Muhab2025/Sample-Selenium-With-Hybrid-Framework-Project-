from pages.homepage import HomePage
from basetest import BaseTest
from util import excel_util

excel_path = "./test_data/datadriven.xlsx" 
excel_sheet = "RegisterTest"

class TestRegistration(BaseTest):
    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_registration_page()
        account_success = register_page.register_account(excel_util.get_cell_data(excel_path, excel_sheet, 2, 1), 
                                                         excel_util.get_cell_data(excel_path, excel_sheet, 2, 2), 
                                                         self.generate_email_with_timestamp(), 
                                                         excel_util.get_cell_data(excel_path, excel_sheet, 2, 3), 
                                                         "12345", "12345", "no", "yes")
        assert account_success.display_account_created_message()

    def test_create_account_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_registration_page()
        account_success = register_page.register_account("Samir", "Hana", self.generate_email_with_timestamp(), "1234567890", "12345", "12345", "yes", "yes")
        assert account_success.display_account_created_message()

    def test_create_account_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_registration_page()
        register_page.register_account("Samir", "Hana", "mohabda19@yahoo.com", "1234567890", "12345", "12345", "no", "yes")
        assert register_page.display_duplicate_email_warning_message()

    def test_register_account_with_empty_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_registration_page()
        register_page.register_account("", "", "", "", "", "", "", "")
        assert register_page.display_all_warning_messages()