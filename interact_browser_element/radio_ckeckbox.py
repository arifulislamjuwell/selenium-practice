from selenium import webdriver
import time

class RadioCheck:

    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'

        driver= webdriver.Chrome()
        
        driver.get(base_url)

        radio_but_1= driver.find_element_by_id("bmwradio")
        radio_but_1.click()
        time.sleep(2)

        radio_but_2= driver.find_element_by_id("hondaradio")
        radio_but_2.click()
        time.sleep(2)

        check_box_1= driver.find_element_by_id("bmwcheck")
        check_box_1.click()
        time.sleep(2)

        check_box_2= driver.find_element_by_id("hondacheck")
        check_box_2.click()
        time.sleep(2)


        print('radio 1 selected: '+ str(radio_but_1.is_selected()))
        print('radio 1 selected: '+ str(radio_but_2.is_selected()))
        print('radio 1 selected: '+ str(check_box_1.is_selected()))
        print('radio 1 selected: '+ str(check_box_2.is_selected()))

obj = RadioCheck()
obj.test()