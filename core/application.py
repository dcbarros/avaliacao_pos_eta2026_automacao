from core.browser import BrowserSession
from pages.add_customer_page import AddCustomerPage
from pages.customers_page import CustomersPage
from pages.login_page import LoginPage
from pages.manager_page import ManagerPage

class XYZBankApp:

    def __init__(self):
        self.__browser = BrowserSession()
        self.login_page: LoginPage | None = None
        self.manager_page: ManagerPage | None = None
        self.add_customer_page: AddCustomerPage | None = None
        self.customers_page: CustomersPage | None = None

    def __enter__(self):
        driver = self.__browser.iniciar()

        try:
            self.login_page = LoginPage(driver)
            self.manager_page = ManagerPage(driver)
            self.add_customer_page = AddCustomerPage(driver)
            self.customers_page = CustomersPage(driver)
        except BaseException:
            self.__browser.fechar()
            raise

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__browser.fechar()
