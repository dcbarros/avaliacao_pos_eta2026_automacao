import pytest

from core.application import XYZBankApp

@pytest.fixture()
def app():
    with XYZBankApp() as app:
        yield app

#@pytest.fixture()
#def login_page(app):
#    app.login_page.open()
#    return app.login_page vishiiii