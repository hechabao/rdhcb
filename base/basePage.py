class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.base_url = 'https://check.rongdasoft.com/'
    def find_URL_element(self,loc):
        return self.driver.find_element(*loc)

    def find_URL_elements(self,loc):
        return self.driver.find_elements(*loc)
