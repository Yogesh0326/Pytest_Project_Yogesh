import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_config
from utilities.custome_logger import Log_Maker
from utilities import excel_utils


class Test_admin_Login_data_driven:
    admin_page_url = Read_config.get_admin_page_url()  # we called url value using read_config file before that import it
    admin_page_url_after_login = Read_config.get_admin_page_url_after_login()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()  # we called static log_gen method using class name Log_maker
    path = ".//test_data//admin_login_data.xlsx"

    @pytest.mark.regression
    def test_valid_login_data_driven(self, setup):
        self.logger.info("##### test_valid_login_data_driven 1 #####")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)

        self.row = excel_utils.get_row_count(self.path, "login_data")
        print("no of rows:", self.row)
        self.status_list = []
        # for r in range(2, self.row + 1):
        self.username = excel_utils.get_read_data(self.path, "login_data", 2, 1)
        self.password = excel_utils.get_read_data(self.path, "login_data", 2, 2)
        self.exp_login = excel_utils.get_read_data(self.path, "login_data", 2, 3)
        print("username", self.username)
        print("password", self.password)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(2)

        if self.exp_login == "Yes":
            self.logger.info("test case passed")
            self.status_list.append('pass')
        else:
            self.logger.info("test case failed")
            self.status_list.append('fail')

        print('status list is ', self.status_list)

        if 'fail' in self.status_list:
            self.logger.info('test admin login data driven test case failed')
            assert False
        else:
            self.logger.info('test admin login data driven test case passed')
            assert True

        self.driver.close()
