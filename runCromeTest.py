from selenium import webdriver
import os

class runCRM:
    
    def test(self):
        driverlocation= '/usr/bin/chromedriver'

        os.environ['webdriver.chrome.driver']= driverlocation
        driver= webdriver.Chrome(driverlocation)

        driver.get('https://docs.celeryproject.org/en/stable/')

obj= runCRM()
obj.test()