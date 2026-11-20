import time

class TestCT08:
    def test_ct08_impedir_saque_maior_que_o_saldo(self, login_page, customers_page, transactions_page):
        login_page.logar_como_usuario_cliente("2")
        customers_page.seleciona_conta_cliente("1004")
        customers_page.depositar_valor_em_conta("500")

        # Passo 1:
        operacao = customers_page.realizar_transferencia("800")

        # Passo 2:
        assert operacao["mensagem"] == "Transaction Failed. You can not withdraw amount more than the balance."
        assert operacao["balanco"] == "500"
        # Passo 3: 
        deposito_realizado = False
        customers_page.acessar_pagina_transacoes()
        transactions_page.validar_quantidade_linhas(1)
        for operacao in transactions_page.coletar_transacoes():
            if(operacao["valor"] == 800 and operacao["tipo"] == "Debit"):
                deposito_realizado = True

        

        assert deposito_realizado == False, "A operação de transferência foi registrada."

    