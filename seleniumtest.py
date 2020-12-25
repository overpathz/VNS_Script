from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from loginpassword import *
from urlslist import *
import time

# path to the chromedriver to selenium works
PATH = "C:\Program Files (x86)\chromedriver.exe"

# discipline list urls
discipline = physics


# main process
def log_in(times):
    for i in range(times):
        for j in discipline:
            driver = webdriver.Chrome(PATH)
            driver.get(j)
            loginField = driver.find_element_by_id('username')
            loginField.clear()
            loginField.send_keys(loginVNS)

            passwordField = driver.find_element_by_id('password')
            passwordField.clear()
            passwordField.send_keys(pswdVNS)
            passwordField.send_keys(Keys.RETURN)
            time.sleep(1)

            driver.close()


log_in(1)
