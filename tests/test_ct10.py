def test_ct10_filtrar_extrato_por_periodo(login_page, transactions_page, account_page):
    # Pré-condição: Hermoine Granger (value="1") conectada, conta 1001, extrato aberto
    login_page.open()
    login_page.logar_como_usuario_cliente("1")
    account_page.selecionar_conta("1001")
    account_page.abrir_extrato()
    assert transactions_page.validar_url_extrato()

    # Passos 1 e 2: Preencher data inicial e final
    transactions_page.filtrar_por_periodo(
        data_inicio_iso="2015-01-02T00:00",
        data_fim_iso="2015-01-03T23:59"
    )

    # Passo 3 e Resultado Esperado: Somente 4 linhas do período
    assert transactions_page.validar_quantidade_linhas(4)
    transacoes = transactions_page.coletar_transacoes()

    esperado = [
        ("Jan 2, 2015", 30, "Credit"),
        ("Jan 2, 2015", 4, "Debit"),
        ("Jan 3, 2015", 30, "Credit"),
        ("Jan 3, 2015", 4, "Debit"),
    ]

    for tx, (data_esp, valor_esp, tipo_esp) in zip(transacoes, esperado):
        assert data_esp in tx["data_hora"]
        assert tx["valor"] == valor_esp
        assert tx["tipo"] == tipo_esp