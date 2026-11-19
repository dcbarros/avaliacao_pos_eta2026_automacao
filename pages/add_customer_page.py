from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "form button[type='submit']")

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
    def adicionar_customer(self, first_name, last_name, post_code):
        self.escrever_texto(self.FIRST_NAME_INPUT, first_name)
        self.escrever_texto(self.LAST_NAME_INPUT, last_name)
        self.escrever_texto(self.POST_CODE_INPUT, post_code)
        self.clicar_no_elemento(self.ADD_CUSTOMER_BUTTON)
