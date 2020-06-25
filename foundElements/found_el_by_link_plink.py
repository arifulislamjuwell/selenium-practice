from selenium import webdriver
import os

class FoundElementByLinkPlink:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/'
        driver= webdriver.Chrome()

        driver.get(base_url)

        element_by_link= driver.find_element_by_link_text('Login')
        if element_by_link is not None:
            print('element found by link')

        element_by_p_link= driver.find_element_by_partial_link_text('Prac')
        if element_by_p_link is not None:
            print('element found by partial link')


obj= FoundElementByLinkPlink()
obj.test()