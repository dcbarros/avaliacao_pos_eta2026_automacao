import time
def test_ct08_impedir_saque_maior_que_o_saldo(login_page, customers_page):
    login_page.logar_como_usuario_cliente("2")
    customers_page.seleciona_conta_cliente("1004")
    customers_page.depositar_valor_em_conta("500")

    # Passo 1:
    operacao = customers_page.realizar_transferencia("800")
    time.sleep(5)
    # Passo 2:
    #assert operacao["mensagem"] == "Transaction Failed. You can not withdraw amount more than the balance."
    #assert operacao["balanco"] == "500"
    # Passo 3: 