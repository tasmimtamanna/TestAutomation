from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class MultipleWindow():
    def multiple_window_handle(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://the-internet.herokuapp.com/windows')
        time.sleep(3)

        parent_window = driver.current_window_handle

        child_window_link = driver.find_element(By.LINK_TEXT, 'Click Here')
        child_window_link.click()

        second_window_link = driver.find_element(By.LINK_TEXT, 'Elemental Selenium')
        second_window_link.click()

        all_windows = driver.window_handles
        time.sleep(2)

        # Switching child_window
        for child_window in all_windows:
            if child_window not in parent_window:
                driver.switch_to.window(child_window)
                time.sleep(4)
                print('Child window Title: ', driver.title)

                # Switching parent_window
        for child_window2 in all_windows:
            if child_window2 not in parent_window:
                driver.switch_to.window(child_window2)
                time.sleep(4)
                print('Child window Title: ', driver.title)

        for child_window in all_windows:
            if child_window not in parent_window:
                driver.switch_to.window(parent_window)
                time.sleep(2)
                print("Parent window Title: ", driver.title)


test_obj = MultipleWindow()
test_obj.multiple_window_handle()
