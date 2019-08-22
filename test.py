import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


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
        assert driver.title == "Fictionlog | นิยายออนไลน์ สุดมันส์ สดใหม่ ฟินทุกรส ครบทุกอารมณ์!", "cannot open this site"

    def test_Login(self):
        driver = self.driver
        key = open("key.txt").read().splitlines()
        driver.find_element_by_xpath("//div[@class='Navbar__NavbarRightMenuBox-sc-1gjhe9u-8 glkmWR']").click()
        username = driver.find_element_by_id("login-username")
        if username:
            print("login box is founded")
        else:
            print("login box not found")
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
            print("search box not found")

        def search(msg):

            first = ""
            driver.find_element_by_xpath("//*[@class='SearchForm__ClearTextButton-sc-1utrbvs-0 jPBmQo']").click()
            driver.find_element_by_xpath("//input[@class='SearchForm__Input-sc-1utrbvs-1 dxqRDK']").send_keys(msg,
                                                                                                              Keys.ENTER)
            driver.implicitly_wait(300)

            # print("1")
            has = driver.find_element_by_xpath(
                "//div[@class='container Search__FeedBox-b4vuer-0 daudpn']/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]").is_displayed()
            # first = driver.find_element_by_xpath(
            #     "//div[@class='container Search__FeedBox-b4vuer-0 daudpn']/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]").text

            while has and msg not in first:
                # print("3")
                driver.implicitly_wait(300)
                first = driver.find_element_by_xpath(
                    "//div[@class='container Search__FeedBox-b4vuer-0 daudpn']/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]").text

            print(first)
            assert msg in first, "maybe this msg be not found or something wrong"

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
            print("search box not found")

        def search(msg):
            driver.find_element_by_xpath("//*[@class='SearchForm__ClearTextButton-sc-1utrbvs-0 jPBmQo']").click()
            driver.find_element_by_xpath("//input[@class='SearchForm__Input-sc-1utrbvs-1 dxqRDK']").send_keys(msg,
                                                                                                              Keys.ENTER)
            driver.implicitly_wait(200)
            element = driver.find_element_by_xpath(
                "//div[@class='container Search__FeedBox-b4vuer-0 daudpn']/div[2]/div[1]")

            assert element.text == "ไม่พบนิยาย", "maybe this msg can found in novel's name or something wrong"

        search("123456789878")

    def test_LoginFail(self):
        driver = self.driver

        driver.find_element_by_xpath("//div[@class='Navbar__NavbarRightMenuBox-sc-1gjhe9u-8 glkmWR']").click()
        username = driver.find_element_by_id("login-username")
        if username:
            print("login box is founded")
        else:
            print("login box  not found")
        username.send_keys("key[0]")
        pwd = driver.find_element_by_id("login-password")
        pwd.send_keys("key[1]")
        driver.find_element_by_xpath("//div[@class='LoginForm__RowWrapper-sc-1yidlb5-4 bxQUXd']/button[1]").click()

        error = driver.find_element_by_xpath("//div[@class='Title__Text-sc-1jzccie-0 Title__H3-sc-1jzccie-3 jNtoco']")
        assert error.text == "เกิดข้อผิดพลาด", "this username and password ขcan login to website"

    def test_Logout(self):
        driver = self.driver
        key = open("key.txt").read().splitlines()
        driver.find_element_by_xpath("//div[@class='Navbar__NavbarRightMenuBox-sc-1gjhe9u-8 glkmWR']").click()
        username = driver.find_element_by_id("login-username")
        if username:
            print("login box is founded")
        else:
            print("login box not found")
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

        logout_btn = driver.find_element_by_xpath(
            "//div[@class='NavbarProfileDropdown__DropdownModalItemsWrapper-sy9wmn-8 lcEttg']/div[3]")  # หาผิดปุ่ม
        # print(logout_btn.text)
        assert logout_btn.text == "ออกจากระบบ", "wrong btn"
        logout_btn.click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath(
            "//*[@class='WithoutLoginNavbar__ButtonBox-sc-1wcn44i-0 WithoutLoginNavbar__LoginButton-sc-1wcn44i-1 jpvUIv']").click()
        txt = driver.find_element_by_xpath("//*[@class='styleModals__ModalTitle-sc-1mu53dz-1 ljhljk']").text
        assert txt == "เข้าสู่ระบบ", "logout not successful"

    def test_ClickToChangeCategory(self):
        driver = self.driver
        topRank = driver.find_element_by_xpath(
            "//div[@id='__next']/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        assert topRank.text == "อันดับนิยายมาแรง", "wrong btn"
        topRank.click()

        header = driver.find_element_by_xpath("//div[@class='ExploreForm__CategoryHeader-txiseh-9 buKqdz']/span[1]")

        assert header.text == "เลือกหมวดนิยาย", "something wrong"
        categories = ['แฟนตาซี', 'กำลังภายใน', 'ไลท์โนเวล', 'กีฬา', 'ไซไฟ', 'ผจญภัย', 'สืบสวน', 'สยองขวัญ', 'สารคดี',
                      'ชีวิต', 'โรแมนติก', 'ดราม่า', 'รักวัยรุ่น', 'คอเมดี้', 'ย้อนยุค', 'Boy Love / Yaoi',
                      'Girl Love / Yuri', 'Idol Fic / Fanfic']
        xpath = "//div[@class='ExploreForm__CategoryList-txiseh-6 kMSoIq']/button[2]"
        category = driver.find_element_by_xpath(xpath)
        category.click()
        print(f"now click {category.text}")
        # xpath = "//div[@class='ExploreForm__CategoryList-txiseh-6 kMSoIq']/button[3]"
        # category = driver.find_element_by_xpath(xpath)
        # category.click()
        # print(f"now click {category.text}")
        # enter_btn = driver.find_element_by_xpath("//div[@class='ExploreForm__Footer-txiseh-5 kpvFKN']/div[5]")
        # actions = ActionChains(driver)
        # actions.move_to_element(enter_btn)
        # actions.click(enter_btn)
        # actions.perform()
        # print(f"now click {enter_btn.text}")
        # driver.implicitly_wait(300)
        # sleep(5)
        for i in range(3, len(categories) + 2):
            xpath = "//div[@class='ExploreForm__CategoryList-txiseh-6 kMSoIq']/button[" + str(i) + "]"
            category = driver.find_element_by_xpath(xpath)
            category.click()
            print(f"now click {category.text}")
            enter_btn = driver.find_element_by_xpath("//div[@class='ExploreForm__Footer-txiseh-5 kpvFKN']/div[5]")
            enter_btn.click()
            print(f"now click {enter_btn.text}")
            sleep(3)
            last_path = "//div[@class='ExploreForm__CategoryList-txiseh-6 kMSoIq']/button[" + str(i-2) + "]"
            last_cat = driver.find_element_by_xpath(last_path)
            first = driver.find_element_by_xpath(
                "//div[@class='CardItem__FeedItemWrapper-sc-17chdn6-12 honvOT']/div[3]/div[1]/div[2]")
            while (not(last_cat.text in first.text)) or (not(category.text in first.text)):
                driver.implicitly_wait(100)
                first = driver.find_element_by_xpath("//div[@class='CardItem__FeedItemWrapper-sc-17chdn6-12 honvOT']/div[3]/div[1]/div[2]")
                print(f"now :{first.text}")
            assert categories[i-2] in first.text




    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
