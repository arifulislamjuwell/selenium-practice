from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

class ClickType:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/'

        driver= webdriver.Chrome()
        
        driver.get(base_url)

        time.sleep(3)
        element_login_button= driver.find_element(By.XPATH, "//a[@class='navbar-link fedora-navbar-link']")
        element_login_button.click()

        element_input_email= driver.find_element(By.XPATH, "/html//input[@id='user_email']")
        element_input_email.send_keys('test')

        element_input_password= driver.find_element(By.XPATH, "/html//input[@id='user_password']")
        element_input_email.send_keys('test')

        time.sleep(3)
        element_input_email.clear()
        time.sleep(3)

        element_input_email.send_keys('test')



obj= ClickType()
obj.test()