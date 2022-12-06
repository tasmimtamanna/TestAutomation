from selenium import webdriver


def firefox_browser():
    driver = webdriver.Firefox(executable_path='F:\\New folder\\test\\drivers\\geckodriver.exe')

    driver.get('http://techntalents.website/techtalents/Codes/')
firefox_browser()
