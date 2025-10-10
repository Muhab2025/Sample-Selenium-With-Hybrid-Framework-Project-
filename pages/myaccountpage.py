from pages.basepage import BasePage

class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_link_text = "Edit your account information"
    
    def display_edit_your_account_message(self):
        return self.element_display_status("edit_your_account_link_text", self.edit_your_account_link_text)
    
   