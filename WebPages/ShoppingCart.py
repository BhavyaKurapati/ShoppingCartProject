import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BaseSetup
from Config.Locators import Shopping_Cart_Locator



class ShoppingPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)

    def added_dresses_to_Cart(self):
        print('add_summer_dresses_to_cart')
        self.do_click(Shopping_Cart_Locator.dresses_link)
        self.do_click(Shopping_Cart_Locator.summer_dresses_link)
        time.sleep(2)
        dresseslist = self.driver.find_element(By.XPATH, "//ul[@class='product_list grid row']")
        items = dresseslist.find_elements(By.XPATH,
                                          "//ul[@class='product_list grid row']//child::li[contains(@class, 'ajax_block_product')]")
        items_len = len(items)
        print('items list is ', items, items_len)
        print('items length is ', items_len)
        for item in range(1, items_len + 1):
            str1 = str(item)
            text = 'li[' + str1 + ']'
            time.sleep(2)
            self.mouse_hover((By.XPATH,"//*[@id='center_column']/ul/" + text))
            time.sleep(2)
            element_location = "//*[@id='center_column']/ul/"+text+"/div/div[2]/div[2]/a[1]/span"
            print(element_location)
            time.sleep(2)
            self.driver.find_element(By.XPATH, element_location).click()
            time.sleep(5)
            self.do_click(Shopping_Cart_Locator.continue_button)
        return items_len
        return self.is_enabled(Shopping_Cart_Locator.shopping_button)
