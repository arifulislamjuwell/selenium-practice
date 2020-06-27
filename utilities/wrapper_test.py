from selenium import webdriver
import time
from generic_method import UseableWrapprs
class Text:

    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'

        driver= webdriver.Chrome()
        driver.get(base_url)

        wp= UseableWrapprs(driver)
        element= wp.get_element('displayed-text', 'id')
        if element:
            print(element)
        driver.quit()

obj = Text()
obj.test()