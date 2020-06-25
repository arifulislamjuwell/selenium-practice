from selenium import webdriver
import os

class FoundElementByXpathCss:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()

        driver.get(base_url)

        element_by_xpath= driver.find_element_by_xpath("/html//table[@id='product']")
        if element_by_xpath is not None:
            print('element found by xpath')

        element_by_css= driver.find_element_by_css_selector('select#carselect')
        if element_by_css is not None:
            print('element found by css')


obj= FoundElementByXpathCss()
obj.test()