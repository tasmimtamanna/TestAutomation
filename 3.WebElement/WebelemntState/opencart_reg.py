from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

class Opencart_Reg():
    def opencart_reg_valid(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://demo.opencart.com/index.php?route=account/register&language=en-gb')


        hyperlink = driver.find_element(By.LINK_TEXT, "login page")
        hyperlink.click()
        time.sleep(2)
        driver.back()

        # FIRSTNAME
        firstname = driver.find_element(By.CSS_SELECTOR, "#input-firstname")

        firstname_display_state = firstname.is_displayed()
        firstname_enable_state = firstname.is_enabled()

        if firstname_display_state and firstname_enable_state == True:
            firstname.send_keys("Tasmim")
        else:
            print("invalid")

        # lastname

        lastname = driver.find_element(By.CSS_SELECTOR, "#input-lastname")

        lastname_display_state = lastname.is_displayed()
        lastname_enable_state = lastname.is_enabled()

        if lastname_display_state and lastname_enable_state == True:
            lastname.send_keys("Islam")
        else:
            print("invalid")

        # EMAIL

        email = driver.find_element(By.CSS_SELECTOR, "#input-email")

        email_enable_state = email.is_enabled()
        email_display_state = email.is_displayed()

        if email_display_state and email_enable_state == True:
            email.send_keys("rokaiyamim6@gmail.com")
        else:
            print("invalid")

        # password

        password = driver.find_element(By.CSS_SELECTOR, "#input-password")
        password_display_state = password.is_displayed()
        password_enable_state = password.is_enabled()

        if password_display_state and password_enable_state == True:
            password.send_keys("Tasmim1019")
        else:
            print("Invalid")
        time.sleep(3)

        # button
        radio_button = driver.find_element(By.XPATH, '//*[@id="form-register"]/fieldset[3]/div/div/div[1]')
        radio_button.click()

        # checkbox
        checkbox = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/div/input')
        checkbox.click()

        privacylink = driver.find_element(By.LINK_TEXT, "Privacy Policy")
        privacylink.click()
        time.sleep(2)

        Close_button = driver.find_element(By.CSS_SELECTOR, "#modal-information > div > div > div.modal-header > button")
        Close_button.click()
        time.sleep(3)

        # continue button
        continue_button = driver.find_element(By.CSS_SELECTOR, "#form-register > div > div > button")
        continue_button.click()

test_obj = Opencart_Reg()
test_obj.opencart_reg_valid()