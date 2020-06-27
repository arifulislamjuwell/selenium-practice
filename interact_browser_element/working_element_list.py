from selenium import webdriver
import time

class ElementList:

    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'

        driver= webdriver.Chrome()
        
        driver.get(base_url)

        radio_buttons= driver.find_elements_by_xpath("//input[contains(@name,'cars') and contains(@type,'radio')]")

        for button in radio_buttons:
            is_selected= button.is_selected()

            if not is_selected:
                button.click()

            time.sleep(2)

obj = ElementList()
obj.test()