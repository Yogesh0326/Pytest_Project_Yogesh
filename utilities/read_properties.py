import configparser
config = configparser.RawConfigParser()  # object create to read ini file
config.read(".\\configurations\\config.ini")  # path of ini file where data is added

# when we call any below method which returns value from config file

class Read_config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url

    @staticmethod
    def get_admin_page_url_after_login():
        url_after_login = config.get('admin login info', 'admin_page_url_after_login')
        return url_after_login

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username