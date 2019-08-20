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

    def test_Login(self):
        driver = self.driver
        key = open("key.txt").read().splitlines()
        # driver.get("https://fictionlog.co/")
        driver.find_element_by_xpath("//div[@class='Navbar__NavbarRightMenuBox-sc-1gjhe9u-8 glkmWR']").click()
        username = driver.find_element_by_id("login-username")
        if username:
            print("login box is founded")
        else:
            print("login box is not founded")
        username.send_keys(key[0])
        pwd = driver.find_element_by_id("login-password")
        pwd.send_keys(key[1])
        driver.find_element_by_xpath("//div[@class='LoginForm__RowWrapper-sc-1yidlb5-4 bxQUXd']/button[1]").click()

        driver.find_element_by_xpath("//div[@class='Avatar__AvatorBox-sc-1u3bppm-0 gGGrfo']").click()
        element = driver.find_element_by_xpath("//div[@class='NavbarProfileDropdown__ProfileId-sy9wmn-5 jwRExF']")
        if "@"+key[0] in element.text:
            print("Login successful")
        else:
            print("Fail")


    # def test_SearchIcon(self):
    #     pass


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
