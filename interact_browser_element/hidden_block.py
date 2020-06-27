from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Dropdown:

    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'

        driver= webdriver.Chrome()
        
        driver.get(base_url)

        input_box= driver.find_element_by_id('displayed-text')
        print('is box found: '+ str(input_box.is_displayed()))

        driver.find_element_by_id('hide-textbox').click()
        print('is box found: '+ str(input_box.is_displayed()))

        driver.find_element_by_id('show-textbox').click()
        print('is box found: '+ str(input_box.is_displayed()))

obj = Dropdown()
obj.test()