from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By


class InteractBrowser:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://www.messenger.com/'
        driver= webdriver.Chrome()
        
        #maximize window
        driver.maximize_window()
        driver.get(base_url)

        try:
            switch= driver.find_element_by_link_text('Switch accounts')
            if switch is not None:
                switch.click()
            time.sleep(2)
        except Exception as e:
            print(e)

        ele_pass= driver.find_element_by_id('email')
        if ele_pass is not None:
            ele_pass.send_keys('juwelariful@yahoo.com')

        time.sleep(2)

        ele_pass= driver.find_element_by_id('pass')
        if ele_pass is not None:
            ele_pass.send_keys('Alone00007')

        time.sleep(2)

        login_button= driver.find_element_by_id('loginbutton')
        if login_button is not None:
            login_button.click()
        
        time.sleep(10)

obj= InteractBrowser()
obj.test()