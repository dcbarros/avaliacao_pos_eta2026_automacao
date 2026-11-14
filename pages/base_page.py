from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def encontrar_elemento(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def encontrar_elementos(self, locator):
        return self._wait.until(EC.visibility_of_all_elements_located(locator))

    def clicar_no_elemento(self, locator):
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def escrever_texto(self, locator, text):
        element = self.encontrar_elemento(locator)
        element.clear()
        element.send_keys(text)

    def limpar_texto(self, locator):
        self.encontrar_elemento(locator).clear()
    
    def esperar_para_contar_elemento(self, locator, count):
        return self._wait.until(
            lambda driver: len(driver.find_elements(*locator)) == count,
            message=f"O locator {locator} não exibiu {count} elemento(s)"
        )
    
    def pegar_url_atual(self):
        return self._driver.current_url
    
    def selecionar_opcao_pelo_valor(self, locator, option_text):
        dropdown = self.encontrar_elemento(locator)
        select = Select(dropdown)
        return select.select_by_value(option_text)

    def selecionar_opcao_pelo_texto_visivel(self, locator, visible_text):
        dropdown = self.encontrar_elemento(locator)
        select = Select(dropdown)
        return select.select_by_visible_text(visible_text)

    def pegar_texto_do_elemento(self, locator):
        return self.encontrar_elemento(locator).text

    def esperar_pela_url(self, url):
        return bool(self._wait.until(EC.url_to_be(url)))

    def elemento_possui_texto(self, locator, text):
        return self._wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"O elemento {locator} não apresentou o texto '{text}'"
        )

    def elemento_possui_atributo(self, locator, attribute, value):
        return bool(self._wait.until(EC.presence_of_element_located(locator)) and
                    self.encontrar_elemento(locator).get_attribute(attribute) == value)

    # Alerts nativos (window.alert) ficam fora do DOM: não têm locator,
    # por isso a leitura é feita trocando o foco do driver para o alert.
    def pegar_texto_do_alerta(self):
        alert = self._wait.until(
            EC.alert_is_present(),
            message="Nenhum alert foi exibido na tela"
        )
        return alert.text

    def confirmar_alerta(self):
        self._wait.until(EC.alert_is_present()).accept()

    def definir_valor_via_js(self, locator, value):
        element = self.encontrar_elemento(locator)
        script = """
        arguments[0].value = arguments[1];
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """
        self._driver.execute_script(script, element, value)