from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Locator():
    def locator_finding(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://techntalents.com/')

        username = driver.find_element(By.XPATH, '//*[@id="container_job_search_results"]/div[3]/div/div/div/div[2]/p[5]/a')
        if username is not None:
            print('succesful')
        else:
            print('unsuccessful')

test_obj= Locator()
test_obj.locator_finding()