from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Base():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,locator):
        element = WebDriverWait(self.driver,20,0.5).until(lambda x:x.find_element(*locator))
        return element

    def is_element(self,locator):
        try:
            element = WebDriverWait(self.driver,20,0.5).until(lambda x:x.find_element(*locator))
            return element
        except:
            return False
    def send_keys(self,locator,text):
        self.find_element(locator).send_keys(text)

    def click(self,locator):
        self.find_element(locator).click()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    bose = Base(driver)
    element_loc = ("id","kw")
    bose.send_keys(element_loc,"chromedriver")
    click_loc = ("id","su")
    bose.click(click_loc)