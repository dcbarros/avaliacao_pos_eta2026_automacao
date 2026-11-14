from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ManagerPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    ADD_CUSTOMER_TAB = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    CUSTOMERS_TAB = (By.CSS_SELECTOR, "button[ng-click='showCust()']")

    def open(self):
        self._driver.get(self.URL)

    def ir_para_add_customer_tab(self):
        self.clicar_no_elemento(self.ADD_CUSTOMER_TAB)

    def ir_para_clientes_tab(self):
        self.clicar_no_elemento(self.CUSTOMERS_TAB)