from selenium import webdriver
import os

class InteractBrowser:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()

        driver.maximize_window()

obj= InteractBrowser()
obj.test()