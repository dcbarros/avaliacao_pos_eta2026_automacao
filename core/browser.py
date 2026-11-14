import os

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BrowserSession:
    def __init__(self):
        self._driver: WebDriver | None = None

    def iniciar(self) -> WebDriver:
        if self._driver is not None:
            raise RuntimeError("A sessão do navegador já foi iniciada.")

        options = webdriver.ChromeOptions()
                
        if os.getenv("HEADLESS", "").lower() in {"1", "true", "yes"}:
            options.add_argument("--headless=new")

        self._driver = webdriver.Chrome(options=options)
        return self._driver

    def fechar(self) -> None:
        if self._driver is not None:
            try:
                self._driver.quit()
            finally:
                self._driver = None