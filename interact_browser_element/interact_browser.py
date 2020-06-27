from selenium import webdriver
import os

class InteractBrowser:
    
    def test(self):

        """set path to /home/juwel/.profile, 
        then dont need to add driverlocation manually on code"""
        # driverlocation= '/usr/bin/chromedriver'
        # os.environ['webdriver.chrome.driver']= driverlocation
        base_url= 'https://letskodeit.teachable.com/p/practice'
        driver= webdriver.Chrome()
        
        #maximize window
        driver.maximize_window()

        #Loads a web page in the current browser session
        driver.get(base_url)

        #Returns the title of the current page.
        title= driver.title

        #Refreshes the current page.       
        driver.refresh()

        #Refreshes the current page.
        driver.get(driver.current_url)
        driver.get('https://www.hackerrank.com/dashboard')
        #Goes one step backward in the browser history.
        driver.back()

        #Goes one step forward in the browser history.
        driver.forward()

        #Gets the source of the current page
        driver.page_source

        # Closes the current window!
        driver.close()

        #Quits the driver and close every associated window.!
        driver.quit()


obj= InteractBrowser()
obj.test()