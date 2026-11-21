def test_ct12_manter_conta_ao_voltar_do_extrato(login_page, account_page, transactions_page):
    login_page.open()
    login_page.logar_como_usuario_cliente("2")

    account_page.selecionar_conta("1005")
    account_page.realizar_deposito(300)

    account_page.esperar_proximo_segundo()

    account_page.abrir_extrato()

    assert transactions_page.validar_url_extrato()
    assert transactions_page.validar_quantidade_linhas(1)
    transacoes = transactions_page.coletar_transacoes()
    assert transacoes[0]["valor"] == 300
    assert transacoes[0]["tipo"] == "Credit"

    transactions_page.clicar_voltar()

    assert account_page.validar_url_conta()
    info = account_page.pegar_texto_info_conta()
    assert "1005" in info
    assert "300" in info
    assert "Pound" in info