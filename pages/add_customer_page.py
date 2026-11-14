from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "form button[type='submit']")

    def adicionar_customer(self, first_name, last_name, post_code):
        self.escrever_texto(self.FIRST_NAME_INPUT, first_name)
        self.escrever_texto(self.LAST_NAME_INPUT, last_name)
        self.escrever_texto(self.POST_CODE_INPUT, post_code)
        self.clicar_no_elemento(self.ADD_CUSTOMER_BUTTON)