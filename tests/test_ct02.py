import re


def test_ct02_abrir_conta_para_um_cliente(login_page, manager_page, customers_page):
    login_page.logar_como_gerente_banco()

    manager_page.ir_para_open_account()
    assert manager_page.esperar_pela_url(manager_page.URL_OPEN_ACCOUNT)

    # Harry Potter tem o ID 2 nos dados iniciais da aplicação.
    mensagem = manager_page.processar_abertura_de_conta("2", "Dollar")
    conta = re.fullmatch(r"Account created successfully with account Number\s*:\s*(\d+)", mensagem)
    assert conta, f"Alerta de abertura de conta inesperado: {mensagem!r}"
    numero_novo = conta.group(1)
    assert numero_novo == "1016"

    manager_page.ir_para_clientes_tab()
    assert customers_page.esperar_pela_url(customers_page.URL)
    assert customers_page.pegar_numeros_de_conta_do_cliente("Harry", "Potter") == [
        "1004", "1005", "1006", numero_novo,
    ]
