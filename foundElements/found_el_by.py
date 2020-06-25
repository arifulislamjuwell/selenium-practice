from selenium import webdriver
import os
from selenium.webdriver.common.by import By
class FoundElementBy:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()

        driver.get(base_url)

        #ID, NAME, XPATH, CSS_SELECTOR, LINK_TEXT
        # PARTIAL_LINK_TEXT, CLASS_NAME, TAG_NAME	
     	#These are	the	attributes available for By	
        element_by_id= driver.find_element(By.ID ,'name')
        if element_by_id is not None:
            print('element found by id')

obj= FoundElementBy()
obj.test()