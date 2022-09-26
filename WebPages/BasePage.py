import random
import string
from os.path import join
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Config.TestData import RegistrationTestdata


class BaseSetup():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(RegistrationTestdata.Base_URl)
        self.driver.maximize_window()

    def wait_for_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element

    def do_click(self, by_locator):
        self.wait_for_element(by_locator).click()

    def do_send_keys(self, by_locator, text):
        self.wait_for_element(by_locator).send_keys(text)

    def select_drop_down(self, by_locator, value):
        element = WebDriverWait(self.driver, 40).until(ec.presence_of_element_located(by_locator))
        self.select = Select(element)
        self.select.select_by_value(str(value))

    def get_element_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text

    def is_enabled(self, by_locator):
        element = self.wait_for_element(by_locator)
        return bool(element)

    def mouse_hover(self, by_locator):
        element = self.wait_for_element(by_locator)
        actions = ActionChains(self.driver).move_to_element(element)
        actions.perform()

    def random_email(self):
        randomtext = ''.join(random.choice(string.ascii_letters) for x in range(10))
        return randomtext + "@domain.com"

    def random_day(self):
        return random.randint(1, 30)


    def random_year(self):
        return random.randint(1900, 2000)

    def get_random_day(self):
        return random.randint(1, 30)

    def get_random_month(self):
        return random.randint(1, 13)

    def get_random_year(self):
        return random.randint(1900, 2021)

    def get_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text

    def teardown(self):
        self.driver.close()
