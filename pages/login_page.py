from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    URL_ACCOUNT = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"

    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    MANAGER_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[ng-click='manager()']")
    CUSTOMER_SELECT = (By.CSS_SELECTOR, "#userSelect")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "form[role='form'] button")

    def open(self):
        self._driver.get(self.URL)

    def logar_como_usuario_cliente(self, option_value):
        self.clicar_no_elemento(self.CUSTOMER_LOGIN_BUTTON)
        self.selecionar_opcao_pelo_valor(self.CUSTOMER_SELECT, option_text=option_value)
        self.clicar_no_elemento(self.LOGIN_BUTTON)
        self.esperar_pela_url(self.URL_ACCOUNT)

    def ir_para_manager(self):
        self.clicar_no_elemento(self.MANAGER_LOGIN_BUTTON)
