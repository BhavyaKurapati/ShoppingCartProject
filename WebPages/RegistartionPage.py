import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BaseSetup
from Config.TestData import RegistrationTestdata
from Config.Locators import Registration_locators, login_locators, Registration_Errors


class Registration(BaseSetup):

    def __init__(self, browser):
        super().__init__(browser)

    def user_registration(self):
        self.do_click(login_locators.signin_link)
        self.do_send_keys(Registration_locators.email_create_account, self.random_email())
        self.do_click(Registration_locators.create_account_button)
        self.do_click(Registration_locators.reg_gender)
        self.do_send_keys(Registration_locators.reg_firstname, RegistrationTestdata.firstname)
        self.do_send_keys(Registration_locators.reg_lastname, RegistrationTestdata.lastname)
        self.do_send_keys(Registration_locators.reg_address, RegistrationTestdata.addressone)
        self.do_send_keys(Registration_locators.reg_password, RegistrationTestdata.password)
        self.do_send_keys(Registration_locators.reg_city, RegistrationTestdata.city)
        self.select_drop_down(Registration_locators.reg_state, self.get_random_day())
        self.do_send_keys(Registration_locators.reg_mobile, RegistrationTestdata.mobile_number)
        self.do_send_keys(Registration_locators.reg_assign_address, RegistrationTestdata.aliasAddress)
        self.do_send_keys(Registration_locators.reg_postcode, RegistrationTestdata.postcode)
        self.do_click(Registration_locators.reg_submit)

    def user_registration_invaliddata(self):
        self.do_click(login_locators.signin_link)
        self.do_send_keys(Registration_locators.email_create_account, self.random_email())
        self.do_click(Registration_locators.create_account_button)
        self.do_click(Registration_locators.reg_gender)
        self.do_send_keys(Registration_locators.reg_firstname, RegistrationTestdata.firstname)
        self.do_send_keys(Registration_locators.reg_lastname, RegistrationTestdata.lastname)
        self.do_send_keys(Registration_locators.reg_address, RegistrationTestdata.addressone)
        self.do_send_keys(Registration_locators.reg_password, RegistrationTestdata.password)
        self.do_send_keys(Registration_locators.reg_city, RegistrationTestdata.city)
        self.select_drop_down(Registration_locators.reg_state, self.get_random_day())
        self.do_send_keys(Registration_locators.reg_mobile, RegistrationTestdata.mobile_number)
        self.do_send_keys(Registration_locators.reg_assign_address, RegistrationTestdata.aliasAddress)
        self.do_send_keys(Registration_locators.reg_postcode, RegistrationTestdata.postcode_invalid)
        self.do_click(Registration_locators.reg_submit)
        time.sleep(2)
        return self.is_enabled(Registration_locators.reg_submit)

    def Registration_Successful(self):
        return self.is_enabled(login_locators.signout_button)

    def Logout_Successful(self):
        self.do_click(login_locators.signout_button)
