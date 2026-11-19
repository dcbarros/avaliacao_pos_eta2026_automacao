import pytest

from core.application import XYZBankApp

@pytest.fixture()
def app():
    with XYZBankApp() as app:
        yield app

@pytest.fixture()
def login_page(app):
    app.login_page.open()
    return app.login_page

@pytest.fixture()
def manager_page(app):
    return app.manager_page

@pytest.fixture()
def customers_page(app):
    return app.customers_page

@pytest.fixture()
def add_customer_page(app):
    return app.add_customer_page

@pytest.fixture()
def transactions_page(app):
    return app.transactions_page

@pytest.fixture()
def deposit_page(app):
    return app.deposit_page