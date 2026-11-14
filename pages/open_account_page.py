from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OpenAccountPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount"

    CUSTOMER_SELECT = (By.CSS_SELECTOR, "#userSelect")
    CURRENCY_SELECT = (By.CSS_SELECTOR, "#currency")
    PROCESS_BUTTON = (By.CSS_SELECTOR, "form button[type='submit']")

    def selecionar_cliente(self, nome_cliente):
        self.selecionar_opcao_pelo_texto_visivel(self.CUSTOMER_SELECT, nome_cliente)

    def selecionar_moeda(self, moeda):
        self.selecionar_opcao_pelo_texto_visivel(self.CURRENCY_SELECT, moeda)

    def clicar_em_process(self):
        self.clicar_no_elemento(self.PROCESS_BUTTON)
