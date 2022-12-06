from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Navigations():
    def navigationcommands(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://techntalents.com/')

        driver.get('https://google.com/')
        driver.back()
        driver.forward()
        driver.refresh()

test_obj = Navigations()
test_obj.navigationcommands()