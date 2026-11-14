from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self._wait.until(EC.visibility_of_all_elements_located(locator))

    def click_element(self, locator):
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def select_dropdown_option(self, locator, option_text):
        dropdown = self.find_element(locator)
        select = Select(dropdown)
        return select.select_by_value(option_text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_for_url(self, url):
        return bool(self._wait.until(EC.url_to_be(url)))

    def element_have_text(self, locator, text):
        return self._wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"O elemento {locator} não apresentou o texto '{text}'"
        )

    def element_have_attribute(self, locator, attribute, value):
        return bool(self._wait.until(EC.presence_of_element_located(locator)) and
                    self.find_element(locator).get_attribute(attribute) == value)
