from pages.searchpage import SearchPage
from pages.loginpage import LogInPage
from pages.registerpage import RegisterPage
from pages.basepage import BasePage 

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class, 'btn-default')]"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.type_in_field(product_name, "search_box_field_name", self.search_box_field_name)

    def click_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)
    
    def searech_for_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_search_button()

    def click_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

    def click_login_option(self):
        self.element_click("login_option_link_text", self.login_option_link_text)
        return LogInPage(self.driver)

    def click_register_option(self):
        self.element_click("register_option_link_text", self.register_option_link_text)
        return RegisterPage(self.driver)
    
    def navigate_to_login_page(self):
        self.click_my_account_drop_menu()
        return self.click_login_option()

    def navigate_to_registration_page(self):
        self.click_my_account_drop_menu()
        return self.click_register_option()



