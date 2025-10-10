from pages.accountsuccesspage import AccountSuccessPage
from pages.basepage import BasePage

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    first_name_input_id = "input-firstname"
    last_name_input_id = "input-lastname"
    email_input_id = "input-email"
    telephone_input_id = "input-telephone"
    password_input_id = "input-password"
    confirm_input_id = "input-confirm"
    agree_input_name = "agree"
    continue_btn_xpath = "//input[@value='Continue']"
    yes_newsletter_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_message_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_message_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_message_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_message_xpath = "//input[@id='input-telephone']/following-sibling::div"    
    password_warning_message_xpath = "//input[@id='input-password']/following-sibling::div"

    duplicate_email_warning_message = "Warning: E-Mail Address is already registered!"
    privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
    first_name_warning_message = "First Name must be between 1 and 32 characters!"
    last_name_warning_message = "Last Name must be between 1 and 32 characters!"
    email_warning_message = "E-Mail Address does not appear to be valid!"
    telephone_warning_message = "Telephone must be between 3 and 32 characters!"
    password_warning_message = "Password must be between 4 and 20 characters!"


    def enter_valid_first_name(self, valid_first_name):
        self.type_in_field(valid_first_name, "first_name_input_id", self.first_name_input_id)

    def enter_valid_last_name(self, valid_last_name):
        self.type_in_field(valid_last_name, "last_name_input_id", self.last_name_input_id)
    
    def enter_valid_email(self, valid_email):
        self.type_in_field(valid_email, "email_input_id", self.email_input_id)

    def enter_valid_telephone(self, valid_telephone):
        self.type_in_field(valid_telephone, "telephone_input_id", self.telephone_input_id)

    def enter_valid_password(self, valid_password):
        self.type_in_field(valid_password, "password_input_id", self.password_input_id)

    def confirm_valid_password(self, valid_password):
        self.type_in_field(valid_password, "confirm_input_id", self.confirm_input_id)

    def click_agree(self):
        self.element_click("agree_input_name", self.agree_input_name)

    def select_yes_newsletter(self):
        self.element_click("yes_newsletter_xpath", self.yes_newsletter_xpath)

    def click_continue(self):
        self.element_click("continue_btn_xpath", self.continue_btn_xpath)
        return AccountSuccessPage(self.driver)

    def register_account(self, first_name, last_name, email, telephone, password, con_password, newsletter, privacy_policy):
        self.enter_valid_first_name(first_name)
        self.enter_valid_last_name(last_name)
        self.enter_valid_email(email)
        self.enter_valid_telephone(telephone)
        self.enter_valid_password(password)
        self.confirm_valid_password(con_password)
        if newsletter.__eq__("yes"):
            self.select_yes_newsletter()
        if privacy_policy.__eq__("yes"):
            self.click_agree()
        return self.click_continue()

    def display_duplicate_email_warning_message(self):
        return self.display_element_message(self.duplicate_email_warning_message, "duplicate_email_warning_message_xpath", self.duplicate_email_warning_message_xpath)

    def display_privacy_policy_warning_message(self):
        return self.display_element_message(self.privacy_policy_warning_message, "privacy_policy_warning_message_xpath", self.privacy_policy_warning_message_xpath)

    def display_first_name_warning_message(self):
        return self.display_element_message(self.first_name_warning_message, "first_name_warning_message_xpath", self.first_name_warning_message_xpath)
    
    def display_last_name_warning_message(self):
        return self.display_element_message(self.last_name_warning_message, "last_name_warning_message_xpath", self.last_name_warning_message_xpath)
    
    def display_email_warning_message(self):
        return self.display_element_message(self.email_warning_message, "email_warning_message_xpath", self.email_warning_message_xpath)
    
    def display_telephone_warning_message(self):
        return self.display_element_message(self.telephone_warning_message, "telephone_warning_message_xpath", self.telephone_warning_message_xpath)
    
    def display_password_warning_message(self):
        return self.display_element_message(self.password_warning_message, "password_warning_message_xpath", self.password_warning_message_xpath)
    
    def display_all_warning_messages(self):
        if (self.display_privacy_policy_warning_message() and
        self.display_first_name_warning_message() and
        self.display_last_name_warning_message() and
        self.display_email_warning_message() and
        self.display_telephone_warning_message() and
        self.display_password_warning_message()):
            return True 
        else:
            return False 
        






   

