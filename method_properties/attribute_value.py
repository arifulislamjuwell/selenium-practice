from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Attribute_Value:

    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'

        driver= webdriver.Chrome()
        
        driver.get(base_url)

        element= driver.find_element(By.ID, "checkbox-example")
        attribute_value= element.get_attribute('class')
        print('attribute name :'+ str(attribute_value))

        driver.quit()
obj = Attribute_Value()
obj.test()