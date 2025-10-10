from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_name, locator_value):
        element = None
        wait = WebDriverWait(self.driver, 10)
        if locator_name.endswith("_id"):
            element = wait.until(EC.presence_of_element_located((By.ID, locator_value)))
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = wait.until(EC.presence_of_element_located((By.NAME, locator_value)))
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator_value)))
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css_selector"):
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element 

    def type_in_field(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def element_display_status(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()
    
    def display_element_message(self, message, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text.__eq__(message)
        

