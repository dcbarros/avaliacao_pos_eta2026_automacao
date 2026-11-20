from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class TransactionsPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx"

    BTN_BACK = (By.CSS_SELECTOR, "button[ng-click='back()']")
    BTN_RESET = (By.CSS_SELECTOR, "button[ng-click='reset()']")
    START_DATE_INPUT = (By.ID, "start")
    END_DATE_INPUT = (By.ID, "end")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tbody tr")

    def validar_url_extrato(self):
        return self.esperar_pela_url(self.URL)

    def clicar_voltar(self):
        self.clicar_no_elemento(self.BTN_BACK)

    def clicar_reset(self):
        self.clicar_no_elemento(self.BTN_RESET)

    def filtrar_por_periodo(self, data_inicio_iso, data_fim_iso):
        self.definir_valor_via_js(self.START_DATE_INPUT, data_inicio_iso)
        self.definir_valor_via_js(self.END_DATE_INPUT, data_fim_iso)

    def selecionar_periodo_disponivel(self):
        data_inicial = self._wait.until(
            lambda driver: driver.find_element(*self.START_DATE_INPUT).get_dom_attribute("min"),
            message="O extrato não informou a data inicial mínima",
        )
        data_final = self._wait.until(
            lambda driver: driver.find_element(*self.END_DATE_INPUT).get_dom_attribute("max"),
            message="O extrato não informou a data final máxima",
        )
        self.filtrar_por_periodo(data_inicial, data_final)

    def validar_quantidade_linhas(self, quantidade):
        try:
            return self.esperar_para_contar_elemento(self.TABLE_ROWS, quantidade)
        except TimeoutException as erro:
            raise AssertionError(
                f"Esperava {quantidade} linha(s) no extrato. "
                f"Transações exibidas: {self.coletar_transacoes()!r}"
            ) from erro

    def coletar_transacoes(self):
        rows = self._driver.find_elements(*self.TABLE_ROWS)
        transacoes = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:
                transacoes.append({
                    "data_hora": cols[0].text.strip(),
                    "valor": int(cols[1].text.strip()),
                    "tipo": cols[2].text.strip(),
                })
        return transacoes
