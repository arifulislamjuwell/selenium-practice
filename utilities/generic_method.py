from selenium.webdriver.common.by import By

class UseableWrapprs:

    def __init__(self, driver):
        self.driver= driver

    def get_locator_type(self, locator_type):
        locator= locator_type.lower()
        if locator == 'id':
            return By.ID
        elif locator == 'xpath':
            return By.XPATH
        elif locator == 'name':
            return By.NAME
        else:
            print('No locator type found')
        return False
    
    def get_element(self, locator, locator_type):
        locator_type= self.get_locator_type(locator_type)
        if locator_type:
            try:
                element= self.driver.find_element(locator_type, locator)
                print('element found')
                return element
            except:
                print('element not found')

        else:
            print('locator type invalid')

        return None