import pytest

from pages.homepage import HomePage      
from basetest import BaseTest
from util import excel_util

excel_path = "./test_data/datadriven.xlsx"  
excel_sheet = "LoginTest"

class TestLogin(BaseTest):
    @pytest.mark.parametrize("email, password", excel_util.get_excel_data(excel_path, excel_sheet))
    @pytest.mark.regression
    def test_login_with_valid_credentials(self, email, password):  
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        my_accout = login_page.login_with_credentials(email, password)
        assert my_accout.display_edit_your_account_message()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_login_with_invalid_email(self): 
        self.logger.info("********************Testing login with invalid email********************")  
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials(self.generate_email_with_timestamp(), "123456")    
        assert login_page.display_invalid_credentials_message()
        self.logger.info("********************Finished testing login with invalid email********************") 

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("mohabda19@yahoo.com", "123564")
        assert login_page.display_invalid_credentials_message()

    def test_login_without_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("", "")
        assert login_page.display_invalid_credentials_message()
    