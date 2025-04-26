import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_config
from utilities.custome_logger import Log_Maker


class Test_admin_Login:
    admin_page_url = Read_config.get_admin_page_url()  # we called url value using read_config file before that import it
    admin_page_url_after_login = Read_config.get_admin_page_url_after_login()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()  # we called static log_gen method using class name Log_maker

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("##### Title verification Test case-1 ######")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        time.sleep(2)
        if act_title == exp_title:
            self.logger.info("##### Title verification title matched #####")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self, setup):
        self.logger.info("##### valid login Test case-2  #####")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(2)
        # act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class= 'content-header']/h1").text
        # if act_dashboard_text == "Dashboard":
        #     self.logger.info("#####  login in application url launch successfully #####")
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_invalid_valid_login(self, setup):
        self.logger.info("##### invalid login Test case-3 #####")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        time.sleep(2)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(2)
        # error_msg = self.driver.find_element(By.XPATH, "//div[@class = 'message-error validation-summary-errors']/ul/li").text
        # if error_msg == "No customer account found":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False
        self.driver.close()
