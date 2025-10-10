from pages.basepage import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"
    invalid_product_xpath = "//input[@id='button-search']/following-sibling::p"
    invalid_product_message = "There is no product that matches the search criteria."

    def display_status_of_valid_product(self):
        return self.element_display_status("valid_hp_product_link_text", self.valid_hp_product_link_text)
    
    def display_invalid_product_message(self):
        return self.display_element_message(self.invalid_product_message, "invalid_product_xpath", self.invalid_product_xpath)
    