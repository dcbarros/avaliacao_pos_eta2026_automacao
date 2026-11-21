import re


def test_ct14_novo_cliente_acessa_conta(app, login_page, manager_page, account_page, add_customer_page):
    login_page.open()
    login_page.ir_para_manager()

    manager_page.ir_para_add_customer()
    texto_cliente = add_customer_page.adicionar_cliente("Aluno", "QA", "50000")
    id_cliente = re.search(r"customer id\s*:?\s*(\d+)", texto_cliente).group(1)

    texto_conta = manager_page.abrir_conta(id_cliente, "Pound")
    numero_conta = int(re.search(r"account Number\s*:?\s*(\d+)", texto_conta).group(1))

    account_page.clicar_home()
    login_page.logar_como_usuario_cliente(id_cliente)

    assert account_page.validar_url_conta()
    assert "Welcome Aluno QA !!" in account_page.pegar_texto_boas_vindas()
    info = account_page.pegar_texto_info_conta()
    assert str(numero_conta) in info
    assert "Balance : 0" in info
    assert "Pound" in info
