from pages.basepage import BasePage
from pages.myaccountpage import MyAccountPage

class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_input_id = "input-email" 
    password_input_id = "input-password"
    login_btn_xpath = "//input[@value='Login']"
    invalid_credentials_message_xpath = "//div[@id='account-login']/div[1]"
    invalid_credentials_message_warning = "Warning: No match for E-Mail Address and/or Password."


    def enter_valid_email(self, valid_email):
        self.type_in_field(valid_email, "email_input_id", self.email_input_id)

    def enter_valid_password(self, valid_password):
        self.type_in_field(valid_password, "password_input_id", self.password_input_id)

    def click_login_btn(self):
        self.element_click("login_btn_xpath", self.login_btn_xpath)
        return MyAccountPage(self.driver)
    
    def login_with_credentials(self, email, password):
        self.enter_valid_email(email)
        self.enter_valid_password(password)
        return self.click_login_btn()

    def display_invalid_credentials_message(self):
        return self.display_element_message(self.invalid_credentials_message_warning, "invalid_credentials_message_xpath", self.invalid_credentials_message_xpath)
    


    