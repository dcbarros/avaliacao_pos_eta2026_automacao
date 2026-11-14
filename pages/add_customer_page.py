from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddCustomerPage(BasePage):

    CAMPO_NOME = (By.XPATH, "//input[@placeholder='First Name']")
    CAMPO_SOBRENOME = (By.XPATH, "//input[@placeholder='Last Name']")
    CAMPO_CEP = (By.XPATH, "//input[@placeholder='Post Code']")
    BOTAO_ADICIONAR = (By.XPATH, "//form//button[normalize-space()='Add Customer']")

    def adicionar_cliente(self, primeiro_nome, sobrenome, cep):
        self.escrever_texto(self.CAMPO_NOME, primeiro_nome)
        self.escrever_texto(self.CAMPO_SOBRENOME, sobrenome)
        self.escrever_texto(self.CAMPO_CEP, cep)
        self.clicar_no_elemento(self.BOTAO_ADICIONAR)
        texto = self.pegar_texto_do_alerta()
        self.confirmar_alerta()
        return texto
