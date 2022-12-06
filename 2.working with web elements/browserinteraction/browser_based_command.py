from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class BrowserInteract():
    def commands(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://techntalents.com/')

        title = driver.title
        print(title)

        url = driver.current_url
        print(url)

        print(driver.page_source)


test_obj= BrowserInteract()
test_obj.commands()