def test_ct12_manter_conta_ao_voltar_do_extrato(app):
    app.login_page.open()
    app.login_page.logar_como_usuario_cliente("2")

    app.account_page.selecionar_conta("1005")
    app.account_page.realizar_deposito(300)

    app.account_page.esperar_proximo_segundo()

    app.account_page.abrir_extrato()

    assert app.transactions_page.validar_url_extrato()
    assert app.transactions_page.validar_quantidade_linhas(1)
    transacoes = app.transactions_page.coletar_transacoes()
    assert transacoes[0]["valor"] == 300
    assert transacoes[0]["tipo"] == "Credit"

    app.transactions_page.clicar_voltar()

    assert app.account_page.validar_url_conta()
    info = app.account_page.pegar_texto_info_conta()
    assert "1005" in info
    assert "300" in info
    assert "Pound" in info