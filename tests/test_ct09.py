from datetime import datetime


def test_ct09_registrar_deposito_e_saque_no_extrato(app):
    # Pré-condição: Navegador novo, Harry Potter (value="2") conectado, conta 1004
    app.login_page.open()
    app.login_page.logar_como_usuario_cliente("2")
    app.account_page.selecionar_conta("1004")

    # Passo 1: Fazer um depósito de 500
    app.account_page.realizar_deposito(500)

    # Passo 2: Clicar em Withdrawl, digitar 200 e clicar em Withdraw
    app.account_page.realizar_saque(200)

    # Resultado Esperado (Passo 2): Mensagem e saldo 300
    assert app.account_page.validar_mensagem_feedback("Transaction successful")
    assert app.account_page.pegar_saldo() == 300

    # Passo 3: Clicar em Transactions
    app.account_page.abrir_extrato()

    # Resultado Esperado (Passo 3): URL #/listTx e 2 linhas (500 Credit e 200 Debit) com data de hoje
    assert app.transactions_page.validar_url_extrato()
    assert app.transactions_page.validar_quantidade_linhas(2)

    transacoes = app.transactions_page.coletar_transacoes()
    hoje = datetime.now()
    data_hoje_formatada = f"{hoje.strftime('%b')} {hoje.day}, {hoje.year}"

    assert transacoes[0]["valor"] == 500
    assert transacoes[0]["tipo"] == "Credit"
    assert data_hoje_formatada in transacoes[0]["data_hora"]

    assert transacoes[1]["valor"] == 200
    assert transacoes[1]["tipo"] == "Debit"
    assert data_hoje_formatada in transacoes[1]["data_hora"]