from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

class FileDownload():
    def download_file(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://the-internet.herokuapp.com/download')
        time.sleep(3)

        download_btn = driver.find_element(By.LINK_TEXT, "logo.png")
        download_btn.click()
        time.sleep(2)

        driver.close()


test_obj = FileDownload()
test_obj.download_file()