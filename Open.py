import os
from selenium import webdriver


def setUp():
    # get the path of chromedriver
    dir = "C:/Users/ARKM/AppData/Roaming/Python/Python37/Scripts"
    chrome_driver_path = dir + "\chromedriver.exe"
    # remove the .exe extension on linux or mac platform
    # create a new Chrome session
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()
    # navigate to the application home page
    driver.get("https://fictionlog.co/")
