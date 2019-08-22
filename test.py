import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



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
        if "Fictionlog | นิยายออนไลน์ สุดมันส์ สดใหม่ ฟินทุกรส ครบทุกอารมณ์!" in driver.title:
            print(driver.title)
        else:
            print(driver.title)

    def test_Login(self):
        driver = self.driver
        key = open("key.txt").read().splitlines()
        driver.find_element_by_xpath("//div[@class='Navbar__NavbarRightMenuBox-sc-1gjhe9u-8 glkmWR']").click()
        username = driver.find_element_by_id("login-username")
        if username:
            print("login box is founded")
        else:
            print("login box is not found")
        username.send_keys(key[0])
        pwd = driver.find_element_by_id("login-password")
        pwd.send_keys(key[1])
        driver.find_element_by_xpath("//div[@class='LoginForm__RowWrapper-sc-1yidlb5-4 bxQUXd']/button[1]").click()

        driver.find_element_by_xpath("//div[@class='Avatar__AvatorBox-sc-1u3bppm-0 gGGrfo']").click()
        element = driver.find_element_by_xpath("//div[@class='NavbarProfileDropdown__ProfileId-sy9wmn-5 jwRExF']")
        if "@" + key[0] in element.text:
            print("Login successful")
        else:
            print("Fail")

    def test_SearchFound(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@class='Navbar__NavbarLeftMenuBox-sc-1gjhe9u-7 SwjX']/a[1]").click()
        element = driver.find_element_by_xpath("//*[@class='EmptyWrapper-sc-88zszt-0 boylLs']")
        if 'ค้นหานิยาย, E-book และผู้ใช้ ได้จาก "กล่องค้นหา" ด้านบน' in element.text:
            print("search box is founded")
        else:
            print("search box is not found")

        def search(msg):

            first = ""
            driver.find_element_by_xpath("//*[@class='SearchForm__ClearTextButton-sc-1utrbvs-0 jPBmQo']").click()
            driver.find_element_by_xpath("//input[@class='SearchForm__Input-sc-1utrbvs-1 dxqRDK']").send_keys(msg,
                                                                                                              Keys.ENTER)
            driver.implicitly_wait(300)



            # print("1")
            has = driver.find_element_by_xpath(
                "//div[@class='container Search__FeedBox-b4vuer-0 daudpn']/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]").is_displayed()

            while has and msg not in first:
                # print("3")
                driver.implicitly_wait(300)
                first = driver.find_element_by_xpath(
                    "//div[@class='container Search__FeedBox-b4vuer-0 daudpn']/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]").text

            print(first)
            assert msg in first

        search("มังกร")
        search("แมว")
        search("แพทย์")
        search("จีน")
        search("เกิดใหม่")

    def test_SearchNotFound(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@class='Navbar__NavbarLeftMenuBox-sc-1gjhe9u-7 SwjX']/a[1]").click()
        element = driver.find_element_by_xpath("//*[@class='EmptyWrapper-sc-88zszt-0 boylLs']")
        if 'ค้นหานิยาย, E-book และผู้ใช้ ได้จาก "กล่องค้นหา" ด้านบน' in element.text:
            print("search box is founded")
        else:
            print("search box is not found")

        def search(msg):
            driver.find_element_by_xpath("//*[@class='SearchForm__ClearTextButton-sc-1utrbvs-0 jPBmQo']").click()
            driver.find_element_by_xpath("//input[@class='SearchForm__Input-sc-1utrbvs-1 dxqRDK']").send_keys(msg,
                                                                                                              Keys.ENTER)
            driver.implicitly_wait(200)
            element = driver.find_element_by_xpath("//div[@class='container Search__FeedBox-b4vuer-0 daudpn']/div[2]/div[1]")

            assert element.text == "ไม่พบนิยาย"

        search("123456789878")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
