from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class CustomersPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"

    ACCOUNT_SELECT = (By.CSS_SELECTOR, "#accountSelect")
    ACCOUNT_INFOS = (By.XPATH, "//*[contains(text(),'Account Number : ')]//strong")
    ACCOUNT_DEPOSIT_BUTTON = (By.XPATH, "//button[contains(text(),'Deposit')]")
    ACCOUNT_WITHDRAWL_BUTTON = (By.XPATH, "//button[contains(text(),'Withdrawl')]")
    ACCOUNT_LABEL = (By.CSS_SELECTOR, '.form-group label')
    ACCOUNT_AMOUNT_INPUT = (By.CSS_SELECTOR, '.form-group input')
    ACCOUNT_AMOUNT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[ng-model='searchCustomer']")
    CUSTOMER_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    CELLS = (By.TAG_NAME, "td")

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

    def realizar_transferencia(self, amount):
        self.clicar_no_elemento(self.ACCOUNT_WITHDRAWL_BUTTON)
        self.elemento_possui_texto(self.ACCOUNT_LABEL, "Amount to be Withdrawn :")
        self.escrever_texto(self.ACCOUNT_AMOUNT_INPUT, amount)
        self.clicar_no_elemento(self.ACCOUNT_AMOUNT_BUTTON)

        return {
            "mensagem" : self.encontrar_elemento(self.AMOUNT_MESSAGE_SUCCESSFUL).text,
            "balanco": self.pegar_informacoes_conta()["balanco"]
        }

    def pesquisar(self, texto):
        self.escrever_texto(self.SEARCH_INPUT, texto)

    def esperar_quantidade_de_clientes(self, quantidade):
        return self.esperar_para_contar_elemento(self.CUSTOMER_ROWS, quantidade)

    def limpar_pesquisa(self):
        self.limpar_texto(self.SEARCH_INPUT)

    def pegar_clientes(self):
        """Retorna (First Name, Last Name, Post Code) de cada cliente exibido na tabela."""
        clientes = []
        for linha in self._driver.find_elements(*self.CUSTOMER_ROWS):
            celulas = linha.find_elements(*self.CELLS)
            clientes.append((celulas[0].text, celulas[1].text, celulas[2].text))
        return clientes


