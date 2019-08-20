import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # openwebsite.setUp()
        dir = "C:/Users/ARKM/AppData/Roaming/Python/Python37/Scripts"
        chrome_driver_path = dir + "/chromedriver.exe"
        # remove the .exe extension on linux or mac platform
        # create a new Chrome session
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://fictionlog.co/")

    def test_OpenWebSite(self):
        driver = self.driver
        # driver.get("https://fictionlog.co/")
        if "Fictionlog | นิยายออนไลน์ สุดมันส์ สดใหม่ ฟินทุกรส ครบทุกอารมณ์!" in  driver.title:
            print(driver.title)
        else:
            print(driver.title)



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
