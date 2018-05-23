# coding:utf-8
from wookapp.common.base import BasePage

class Page_home(BasePage):
    login_text_loc = ("link text","Login")
    registar_text_loc = ("link text",'Registrasi')
    skip_text_loc = ('link text','Skip ')

    def click_login(self):
        self.click(self.login_text_loc)

    def click_registrasi(self):
        self.click(self.registar_text_loc)

    def click_skip(self):
        self.click(self.skip_text_loc)

    def get_logintext(self):
        self.get_text(self.login_text_loc)

    def get_registartext(self):
        self.get_text(self.registar_text_loc)

    def get_skiptext(self):
        self.get_text(self.skip_text_loc)


if __name__ == "__main__":
    size = (480,960)
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://m.wook.id",)
    s = Page_home
    a = s.get_registartext(1)
    print(a)
    # abse_driver.opensize("https://m.wook.id",size)
    input_loc = ("link text","Login")
