from pages.basepage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    your_account_created_message_xpath = "//div[@id='content']/h1"
    your_account_created_message = "Your Account Has Been Created!"

    def display_account_created_message(self):
        return self.display_element_message(self.your_account_created_message, "your_account_created_message_xpath", self.your_account_created_message_xpath)
    