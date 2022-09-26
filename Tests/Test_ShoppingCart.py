import pytest
from Tests.BaseTest import BaseTest
from WebPages.ShoppingCart import ShoppingPage
from WebPages.LoginPage import LoginPage


class Test_ShoppingCart(BaseTest):

    "Validate shopping Cart functionality"

    @pytest.mark.positive
    def test_shoppingcart(self):
        self.login = LoginPage(self.driver)
        self.login.user_Login()
        self.shoppingcart = ShoppingPage(self.driver)
        assert self.shoppingcart.added_dresses_to_Cart()


