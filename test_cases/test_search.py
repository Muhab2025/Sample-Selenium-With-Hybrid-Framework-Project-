from pages.homepage import HomePage
from basetest import BaseTest

class TestSearch(BaseTest):
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver) 
        search_page = home_page.searech_for_product("HP") 
        assert search_page.display_status_of_valid_product()

    def test_search_invalid_product(self): 
        home_page = HomePage(self.driver) 
        search_page = home_page.searech_for_product("Honda") 
        assert search_page.display_invalid_product_message()

    def test_search_without_providing_product(self): 
        home_page = HomePage(self.driver)  
        search_page = home_page.searech_for_product("")
        assert search_page.display_invalid_product_message()

        