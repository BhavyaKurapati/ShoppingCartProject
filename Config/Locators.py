from selenium.webdriver.common.by import By


class login_locators:
    signin_link = (By.XPATH, "//a[@class='login']")
    email_id = (By.ID, "email")
    password = (By.ID, "passwd")
    login_button = (By.ID, "SubmitLogin")
    signout_button = (By.XPATH, "//a[@class='logout']")


class Registration_locators:
    email_create_account = (By.ID, "email_create")
    create_account_button = (By.ID, "SubmitCreate")
    reg_gender = (By.ID, 'uniform-id_gender2')
    reg_firstname = (By.ID, "customer_firstname")
    reg_lastname = (By.ID, "customer_lastname")
    reg_password = (By.ID, "passwd")
    reg_dob_day = (By.ID, "days")
    reg_dob_month = (By.XPATH, "//*[@id='months']")
    reg_dob_years = (By.ID, "years")
    reg_address = (By.ID, "address1")
    reg_city = (By.ID, "city")
    reg_country = (By.ID, "id_country")
    reg_state = (By.ID, "id_state")
    reg_mobile = (By.ID, "phone_mobile")
    reg_postcode = (By.ID, "postcode")
    reg_assign_address = (By.ID, "alias")
    reg_submit = (By.ID, "submitAccount")


class Shopping_Cart_Locator:
    dresses_link = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a")
    summer_dresses_link = (By.XPATH, "//*[@id='categories_block_left']//child::div//child::ul//child::li[3]")
    continue_button = (By.XPATH, "//span[@class='continue btn btn-default button exclusive-medium']")
    shopping_button = (By.XPATH, "//*[@id='order_step']/li[1]/span")
