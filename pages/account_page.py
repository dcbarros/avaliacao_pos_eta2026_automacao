from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"

    ACCOUNT_SELECT = (By.ID, "accountSelect")
    ACCOUNT_INFO_BAR = (By.CSS_SELECTOR, "div[ng-hide='noAccount'].center")

    # Abas de operação
    BTN_TRANSACTIONS = (By.CSS_SELECTOR, "button[ng-click='transactions()']")
    BTN_DEPOSIT_TAB = (By.CSS_SELECTOR, "button[ng-click='deposit()']")
    BTN_WITHDRAWL_TAB = (By.CSS_SELECTOR, "button[ng-click='withdrawl()']")

    # Formulário e mensagens
    AMOUNT_INPUT = (By.CSS_SELECTOR, "input[ng-model='amount']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "form[ng-submit] button[type='submit']")
    FEEDBACK_MESSAGE = (By.CSS_SELECTOR, "span[ng-show='message']")

    BOAS_VINDAS = (By.XPATH, "//strong[contains(normalize-space(),'Welcome')]")
    AVISO_SEM_CONTA = (By.XPATH, "//*[normalize-space(text())='Please open an account with us.']")

    def pegar_texto_boas_vindas(self):
        return self.pegar_texto_do_elemento(self.BOAS_VINDAS)

    def pegar_texto_aviso_sem_conta(self):
        return self.pegar_texto_do_elemento(self.AVISO_SEM_CONTA)

    def operacoes_bancarias_visiveis(self):
        botoes = {
            "Transactions": self.BTN_TRANSACTIONS,
            "Deposit": self.BTN_DEPOSIT_TAB,
            "Withdrawl": self.BTN_WITHDRAWL_TAB,
        }
        return [
            nome for nome, locator in botoes.items()
            if any(botao.is_displayed() for botao in self._driver.find_elements(*locator))
        ]

    def validar_url_conta(self):
        return self.esperar_pela_url(self.URL)

    def selecionar_conta(self, numero_conta):
        self.selecionar_opcao_pelo_valor(self.ACCOUNT_SELECT, f"number:{numero_conta}")

    def pegar_texto_info_conta(self):
        return self.pegar_texto_do_elemento(self.ACCOUNT_INFO_BAR)

    def pegar_saldo(self):
        info_el = self.encontrar_elemento(self.ACCOUNT_INFO_BAR)
        strongs = info_el.find_elements(By.TAG_NAME, "strong")
        return int(strongs[1].text.strip())

    def realizar_deposito(self, valor):
        self.clicar_no_elemento(self.BTN_DEPOSIT_TAB)
        self.elemento_possui_texto(self.SUBMIT_BTN, "Deposit")
        self.escrever_texto(self.AMOUNT_INPUT, str(valor))
        self.clicar_no_elemento(self.SUBMIT_BTN)

    def realizar_saque(self, valor):
        self.clicar_no_elemento(self.BTN_WITHDRAWL_TAB)
        self.elemento_possui_texto(self.SUBMIT_BTN, "Withdraw")
        self.escrever_texto(self.AMOUNT_INPUT, str(valor))
        self.clicar_no_elemento(self.SUBMIT_BTN)

    def validar_mensagem_feedback(self, mensagem_esperada):
        return self.elemento_possui_texto(self.FEEDBACK_MESSAGE, mensagem_esperada)

    def abrir_extrato(self):
        self.clicar_no_elemento(self.BTN_TRANSACTIONS)
