from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def firefox_wdm():
  driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

firefox_wdm()