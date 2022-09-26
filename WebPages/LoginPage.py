import time
from WebPages.BasePage import BaseSetup
from Config.TestData import LoginTestData
from Config.Locators import login_locators


class LoginPage(BaseSetup):

    def user_Login(self):
        self.do_click(login_locators.signin_link)
        self.do_send_keys(login_locators.email_id, LoginTestData.username)
        self.do_send_keys(login_locators.password, LoginTestData.password)
        self.do_click(login_locators.login_button)
        time.sleep(2)


    def invalid_unsuccessfulLogin(self):
        self.do_click(login_locators.signin_link)
        self.do_send_keys(login_locators.email_id, LoginTestData.invalidusername)
        self.do_send_keys(login_locators.password, LoginTestData.invalidpassword)
        self.do_click(login_locators.login_button)
        return self.is_enabled(login_locators.signin_link)

    def invalid_user_unsuccessfulLogin(self):
        self.do_click(login_locators.signin_link)
        self.do_send_keys(login_locators.email_id, LoginTestData.invalidusername)
        self.do_send_keys(login_locators.password, LoginTestData.password)
        self.do_click(login_locators.login_button)
        return self.is_enabled(login_locators.signin_link)

    def invalid_password_unsuccessfulLogin(self):
        self.do_click(login_locators.signin_link)
        self.do_send_keys(login_locators.email_id, LoginTestData.username)
        self.do_send_keys(login_locators.password, LoginTestData.invalidpassword)
        self.do_click(login_locators.login_button)
        return self.is_enabled(login_locators.signin_link)

    def Login_Successful(self):
        return self.is_enabled(login_locators.signout_button)

    def user_logout(self):
        self.do_click(login_locators.signout_button)
        return self.is_enabled(login_locators.signin_link)
