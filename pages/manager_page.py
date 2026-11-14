from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ManagerPage(BasePage):

    ABA_ADD_CUSTOMER = (
        By.XPATH,
        "//button[contains(@class,'tab') and normalize-space()='Add Customer']",
    )
    ABA_OPEN_ACCOUNT = (
        By.XPATH,
        "//button[contains(@class,'tab') and normalize-space()='Open Account']",
    )
    SELECIONAR_CLIENTE = (By.CSS_SELECTOR, "#userSelect")
    SELECIONAR_MOEDA = (By.CSS_SELECTOR, "#currency")
    BOTAO_PROCESSAR = (By.XPATH, "//form//button[normalize-space()='Process']")

    def ir_para_add_customer(self):
        self.clicar_no_elemento(self.ABA_ADD_CUSTOMER)

    def abrir_conta(self, id_cliente, moeda):
        self.clicar_no_elemento(self.ABA_OPEN_ACCOUNT)
        self.selecionar_opcao_pelo_valor(self.SELECIONAR_CLIENTE, id_cliente)
        self.selecionar_opcao_pelo_valor(self.SELECIONAR_MOEDA, moeda)
        self.clicar_no_elemento(self.BOTAO_PROCESSAR)
        texto = self.pegar_texto_do_alerta()
        self.confirmar_alerta()
        return texto
