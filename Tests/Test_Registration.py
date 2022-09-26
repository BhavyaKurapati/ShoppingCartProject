import pytest
from WebPages.RegistartionPage import Registration
from Tests.BaseTest import BaseTest


class Test_Registration(BaseTest):

    "Validate Registration functionality with Valid details"

    @pytest.mark.positive
    def test_registration(self):
        self.registration = Registration(self.driver)
        self.registration.user_registration()
        assert self.registration.Registration_Successful()
        self.registration.Logout_Successful()

    "Validate Registration functionality with inValid details(provided invalid postcode)"

    @pytest.mark.negative
    def test_registration_Invaliddata(self):
        self.registration = Registration(self.driver)
        assert self.registration.user_registration_invaliddata()





