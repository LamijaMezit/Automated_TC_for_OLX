from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestOLXSearch:
    def __init__(self, selenium_driver):
        self.selenium_driver = selenium_driver
        self.wait = WebDriverWait(self.selenium_driver, 10)
    
    def test_olx_search(self):
        self.selenium_driver.get("https://olx.ba/shopovi")
        self.selenium_driver.maximize_window()


        search_term = 'laptop'
        search_input = self.selenium_driver.find_element(By.CSS_SELECTOR, "input[placeholder='Pretraga']")
        search_input.send_keys(search_term)
        assert search_input.get_attribute('value') == search_term

        search_button_locator = "//button[contains(@class, 'header-search-submit')]"
        try:
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, search_button_locator)))
            search_button.click()
        except TimeoutException:
            print("Gumb za pretragu nije bio klikabilan unutar zadanih 10 sekundi.")
        
        wrap_element_locator = ".wrap"
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, wrap_element_locator)))
        except TimeoutException:
            print("Greška  ----->")

        search_results = self.selenium_driver.find_elements(By.CSS_SELECTOR, wrap_element_locator)
       




    



    


        

        




