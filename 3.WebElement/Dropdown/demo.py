from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Demo():
    def dropdown_test_valid(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://the-internet.herokuapp.com/dropdown')
        time.sleep(5)

        dropdown_option = driver.find_element(By.CSS_SELECTOR,"select#dropdown")

        all_option = Select(dropdown_option)

        #all_option.select_by_value("1")

        #all_option.select_by_index(2)

        all_option.select_by_visible_text("Option 1")


test_obj =Demo()
test_obj.dropdown_test_valid()