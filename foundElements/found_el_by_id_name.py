from selenium import webdriver
import os

class FoundElementByIdName:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()

        driver.get(base_url)

        element_by_id= driver.find_element_by_id('name')
        if element_by_id is not None:
            print('element found by id')

        element_by_name= driver.find_element_by_name('show-hide')
        if element_by_name is not None:
            print('element found by name')


obj= FoundElementByIdName()
obj.test()