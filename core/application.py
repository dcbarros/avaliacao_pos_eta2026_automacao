from core.browser import BrowserSession

class XYZBankApp:

    def __init__(self):
        self.__browser = BrowserSession()
        # construtor das pages

    def __enter__(self):
        driver = self.__browser.start()

        # try:
        # instanciar os pages
        # except BaseException:
        #     self.__browser.close()
        #     raise

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__browser.close()