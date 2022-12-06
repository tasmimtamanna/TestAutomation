from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def chrome_wdm():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome_wdm()