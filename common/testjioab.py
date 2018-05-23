from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://m.wook.id")
driver.set_window_size(480,960)
time.sleep(5)

def ll(*loc):
    loc =  ("lick text","Login")
    a = driver.find_element(*loc).click()
    print(a)

ll("lick text","Login")