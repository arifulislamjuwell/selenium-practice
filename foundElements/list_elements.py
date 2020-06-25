from selenium import webdriver
import os

class ListElements:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()

        driver.get(base_url)

        elements_by_class= driver.find_elements_by_class_name('inputs')
        length= len(elements_by_class)
        if elements_by_class is not None:
            print('element founded, the length is: '+str(length))

        elements_by_tag= driver.find_elements_by_tag_name('td')
        length_1= len(elements_by_tag)
        if elements_by_tag is not None:
            print('element founded, the length is: '+str(length_1))


obj= ListElements()
obj.test()