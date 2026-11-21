def test_ct11_limpar_transacoes_reset(login_page, account_page, transactions_page):
    # Pré-condição: Harry Potter (value="2") conectado e depósito de 500 na conta 1004
    login_page.open()
    login_page.logar_como_usuario_cliente("2")
    account_page.selecionar_conta("1004")
    account_page.realizar_deposito(500)

    # Passo 1: Clicar em Transactions
    account_page.abrir_extrato()
    assert transactions_page.validar_url_extrato()

    # Passo 2: Clicar em Reset e validar tabela vazia (0 linhas)
    transactions_page.clicar_reset()
    assert transactions_page.validar_quantidade_linhas(0)

    # Passo 3: Clicar em Back e validar URL #/account e saldo zerado
    transactions_page.clicar_voltar()
    assert account_page.validar_url_conta()

    info_conta = account_page.pegar_texto_info_conta()
    assert "Account Number : 1004" in info_conta
    assert "Balance : 0" in info_conta
    assert "Currency : Dollar" in info_conta