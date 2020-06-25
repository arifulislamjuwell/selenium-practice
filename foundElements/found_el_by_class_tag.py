from selenium import webdriver
import os

class FoundElementByClassTag:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()

        driver.get(base_url)

        element_by_class= driver.find_element_by_class_name('displayed-class')
        element_by_class.send_keys('Test')
        if element_by_class is not None:
            print('element found by class')

        element_by_tag= driver.find_element_by_tag_name('h1')
        text= element_by_tag.text
        if element_by_tag is not None:
            print('element found by tag, value is :' + text)


obj= FoundElementByClassTag()
obj.test()