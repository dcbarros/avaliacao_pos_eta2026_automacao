import re


def test_ct14_novo_cliente_acessa_conta(app):
    app.login_page.open()
    app.login_page.ir_para_manager()

    app.manager_page.ir_para_add_customer_tab()
    texto_cliente = app.add_customer_page.adicionar_cliente("Aluno", "QA", "50000")
    id_cliente = re.search(r"customer id\s*:?\s*(\d+)", texto_cliente).group(1)

    texto_conta = app.manager_page.abrir_conta(id_cliente, "Pound")
    numero_conta = int(re.search(r"account Number\s*:?\s*(\d+)", texto_conta).group(1))

    app.account_page.clicar_home()
    app.login_page.logar_como_usuario_cliente(id_cliente)

    assert app.account_page.validar_url_conta()
    assert "Welcome Aluno QA !!" in app.account_page.pegar_texto_boas_vindas()
    info = app.account_page.pegar_texto_info_conta()
    assert str(numero_conta) in info
    assert "Balance : 0" in info
    assert "Pound" in info
