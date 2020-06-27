from selenium import webdriver
import time

class EnableDisable:

    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://www.google.com/'

        driver= webdriver.Chrome()
        
        driver.get(base_url)

        dis_ena_element= driver.find_element_by_xpath("/html//form[@id='tsf']//div[@class='A8SBwf']//input[@role='combobox']")
        check= dis_ena_element.is_enabled()
        print(check)
        time.sleep(6)

obj = EnableDisable()
obj.test()