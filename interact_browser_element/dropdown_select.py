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

        dropdown= driver.find_element_by_id("carselect")
        select = Select(dropdown)

        select.select_by_value('benz')
        time.sleep(2)

        select.select_by_index('0')
        time.sleep(2)

        select.select_by_visible_text('Honda')
        time.sleep(2)

        select.select_by_index(1)
        time.sleep(2)

obj = Dropdown()
obj.test()