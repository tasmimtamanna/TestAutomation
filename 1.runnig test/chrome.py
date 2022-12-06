from selenium import webdriver

def chrome_browser():
    driver = webdriver.Chrome(executable_path='F:\\New folder\\test\\drivers\\chromedriver.exe')
    driver.get('http://techntalents.website/techtalents/Codes/')
chrome_browser()