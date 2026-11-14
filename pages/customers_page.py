from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class CustomersPage(BasePage):

    ACCOUNT_SELECT = (By.CSS_SELECTOR, "#accountSelect")
    ACCOUNT_INFOS = (By.XPATH, "//*[contains(text(),'Account Number : ')]//strong")
    ACCOUNT_DEPOSIT_BUTTON = (By.XPATH, "//button[contains(text(),'Deposit')]")
    ACCOUNT_AMOUNT_INPUT = (By.CSS_SELECTOR, '.form-group input')
    ACCOUNT_AMOUNT_BUTTON = (By.XPATH, '//button[@type="submit"]')

    AMOUNT_MESSAGE_SUCCESSFUL = (By.CSS_SELECTOR, '[ng-show="message"]')

    def pegar_url(self):
        return self.pegar_url_atual()
    
    def seleciona_conta_cliente(self, account_number):
        return self.selecionar_opcao_pelo_texto_visivel(self.ACCOUNT_SELECT, account_number)

    def pegar_informacoes_conta(self):
        dados = self.encontrar_elementos(self.ACCOUNT_INFOS)

        return {
            "numero_conta": dados[0].text,
            "balanco": dados[1].text,
            "moeda": dados[2].text
        }

    def pegar_informacoes_input_amount(self):
        return self.encontrar_elemento(self.ACCOUNT_AMOUNT_INPUT).get_property("value")

    def depositar_valor_em_conta(self, amount):
        self.clicar_no_elemento(self.ACCOUNT_DEPOSIT_BUTTON)
        self.escrever_texto(self.ACCOUNT_AMOUNT_INPUT, amount)
        self.clicar_no_elemento(self.ACCOUNT_AMOUNT_BUTTON)
        
        return(
            self.elemento_possui_texto(self.AMOUNT_MESSAGE_SUCCESSFUL, "Deposit Successful") and
            self.pegar_informacoes_conta()["balanco"] == amount
        )


