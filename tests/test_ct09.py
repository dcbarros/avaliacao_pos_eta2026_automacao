from datetime import datetime


def test_ct09_registrar_deposito_e_saque_no_extrato(login_page, customers_page, transactions_page):
    # Pré-condição: Navegador novo, Harry Potter (value="2") conectado, conta 1004
    login_page.logar_como_usuario_cliente("2")
    customers_page.seleciona_conta_cliente("1004")

    # Passo 1: Fazer um depósito de 500
    assert customers_page.depositar_valor_em_conta("500"), "Depósito de 500 não confirmado"

    # Passo 2: Clicar em Withdrawl, digitar 200 e clicar em Withdraw
    operacao = customers_page.realizar_transferencia("200")

    # Resultado Esperado (Passo 2): Mensagem e saldo 300
    assert operacao["mensagem"] == "Transaction successful"
    assert operacao["balanco"] == "300"

    # Passo 3: Clicar em Transactions
    # O extrato calcula o limite da data final ao abrir e descarta os milissegundos.
    customers_page.esperar_proximo_segundo()
    customers_page.acessar_pagina_transacoes()

    # Resultado Esperado (Passo 3): URL #/listTx e 2 linhas (500 Credit e 200 Debit) com data de hoje
    assert transactions_page.validar_url_extrato()
    transactions_page.selecionar_periodo_disponivel()
    assert transactions_page.validar_quantidade_linhas(2)

    transacoes = transactions_page.coletar_transacoes()
    hoje = datetime.now()
    data_hoje_formatada = f"{hoje.strftime('%b')} {hoje.day}, {hoje.year}"

    assert transacoes[0]["valor"] == 500
    assert transacoes[0]["tipo"] == "Credit"
    assert data_hoje_formatada in transacoes[0]["data_hora"]

    assert transacoes[1]["valor"] == 200
    assert transacoes[1]["tipo"] == "Debit"
    assert data_hoje_formatada in transacoes[1]["data_hora"]
