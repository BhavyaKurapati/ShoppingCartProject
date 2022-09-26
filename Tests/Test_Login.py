import pytest
from WebPages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class Test_Login(BaseTest):

    "Validate Login functionality with valid username and valid password"

    @pytest.mark.positive
    def test_Login(self):
        self.login = LoginPage(self.driver)
        self.login.user_Login()
        assert self.login.Login_Successful()

    "Validate Logout functionality"

    @pytest.mark.positive
    def test_Logout(self):
        self.login = LoginPage(self.driver)
        assert self.login.user_logout()

    "Validate Login functionality with inValid username and invalid password"

    @pytest.mark.negative
    def test_invalid_Login(self):
        self.login = LoginPage(self.driver)
        assert self.login.invalid_unsuccessfulLogin()

    "Validate Login functionality with inValid username and valid password"

    @pytest.mark.negative
    def test_invalid_User_Login(self):
        self.login = LoginPage(self.driver)
        assert self.login.invalid_user_unsuccessfulLogin()

    "Validate Login functionality with Valid username and invalid password"

    @pytest.mark.negative
    def test_invalid_password_Login(self):
        self.login = LoginPage(self.driver)
        assert self.login.invalid_password_unsuccessfulLogin()
