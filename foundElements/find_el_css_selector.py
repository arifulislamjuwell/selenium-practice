from selenium import webdriver
import os

class FoundCssSelector:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()

        driver.get(base_url)

        element_by_css_selector_1= driver.find_element_by_css_selector("input[class='inputs']")
        if element_by_css_selector_1 is not None:
            print('element found by css selector 1')
        
        element_by_css_selector_2= driver.find_element_by_css_selector("input.inputs")
        if element_by_css_selector_2 is not None:
            print('element found by css selector 2')


        element_by_css_selector_3= driver.find_element_by_css_selector("a.btn-style.class1.class2")
        if element_by_css_selector_3 is not None:
            print('element found by css selector 3')
        
        element_by_css_selector_4= driver.find_element_by_css_selector("input[name*='ide']")
        if element_by_css_selector_4 is not None:
            print('element found by css selector 4')

        element_by_css_selector_5= driver.find_element_by_css_selector("fieldset>button")
        if element_by_css_selector_5 is not None:
            print('element found by css selector 5')


obj= FoundCssSelector()
obj.test()