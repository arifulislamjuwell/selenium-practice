from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Text:

    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'

        driver= webdriver.Chrome()
        
        driver.get(base_url)

        element= driver.find_element(By.XPATH, "/html//table[@id='product']//td[.='Selenium WebDriver With Java']")
        text= element.text
        print('first course name is :'+ str(text))

        driver.quit()
obj = Text()
obj.test()