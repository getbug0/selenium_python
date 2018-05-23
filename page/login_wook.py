from wookapp.common.base import BasePage

class Page_wooklogin(BasePage):
    username_loc = ("id","userName")
    password_loc = ("id","password")
    masuk_loc = ("id","submit")
    forgetPassword_loc = ("id","forgetPassword")

    def sendkeys_username(self):
        self.send_keys(self.username_loc)
    def sendkeys_password(self):
        self.send_keys(self.password_loc)
    def click_masuk(self):
        self.click(self.masuk_loc)

    def find_usertext(self):
        a = self.get_text(self.username_loc)
        if a == "E-mail/Phone number":
            print("deng")
        else:
            print("budeng")