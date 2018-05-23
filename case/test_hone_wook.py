from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from wookapp.page.home_wook_app import Page_home
from wookapp.page.login_wook import Page_wooklogin
url = "https://m.wook.id"
size_loc = (480,960)
class Home_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_driver = Page_home(self.driver)
        self.home_driver.opensize(url,size_loc)
        # self.login_driver = Page_wooklogin(self.driver)
    def tearDown(self):
        self.driver.quit()

    # def test_login01(self):
    #     """判断home页面login按钮文本"""
    #     a = self.home_driver.get_logintext()
    #     print(a)
    #     self.assertEqual(a,"Login")
    #
    # def test_login02(self):
    #     """判断home页面Registrasi按钮文本"""
    #     a = self.home_driver.get_registartext()
    #     print(a)
    #     self.assertEqual(a,"Registrasi")
    #
    # def test_login03(self):
    #     """判断home页面skip按钮文本"""
    #     a = self.home_driver.get_skiptext()
    #     print(a)
    #     self.assertEqual(a,"Skip ")

    def test_login04(self):
        '''点击login'''
        self.home_driver.click_login()
        a=self.home_driver.get_title()
        print(a)
        self.assertEqual(a,"Login")
    def test_login05(self):
        '''点击Registrasi'''
        sy_loc = ("id","headerTitle")
        self.home_driver.click_registrasi()
        a = self.home_driver.get_text(sy_loc)
        print(a)
        self.assertEqual(a,"Syarat dan Ketentuan Pengguna")
    # def test_login02(self):
    #     '''判断user输入框中的值'''
    #     a = self.login_driver.find_usertext()
    #     self.assertEqual(a,"E-mail/Phone number")

    def test_login06(self):
        '''点击Sikp'''
        self.home_driver.click_skip()
        a = self.home_driver.get_title()
        print(a)
        self.assertEqual(a,"WOOK")
if __name__ == "__main__":
    unittest.main()