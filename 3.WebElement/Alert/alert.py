from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

class Alert():
    def alert_handle(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        time.sleep(3)

        #normal alert

        normal_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > button")
        normal_alert.click()
        driver.switch_to.alert.accept()

        time.sleep(2)

        #confirm alert

        confirm_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > button")
        confirm_alert.click()
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        # prompt alert

        Prompt_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(3) > button")
        Prompt_alert.click()
        driver.switch_to.alert.send_keys("Tasmim Islam")
        driver.switch_to.alert.accept()

        time.sleep(2)

        link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
        link.click()

test_obj = Alert()
test_obj.alert_handle()