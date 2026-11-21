import re


def test_ct15_cliente_sem_conta_recebe_aviso(
    login_page, manager_page, add_customer_page, account_page
):
    login_page.ir_para_manager()
    manager_page.ir_para_add_customer()
    mensagem = add_customer_page.adicionar_cliente("Sem", "Conta", "123")
    cliente = re.search(r"customer id\s*:?\s*(\d+)", mensagem)
    assert cliente, f"Alerta de cadastro inesperado: {mensagem!r}"

    account_page.clicar_home()
    login_page.logar_como_usuario_cliente(cliente.group(1))

    assert account_page.validar_url_conta()
    assert account_page.pegar_texto_boas_vindas() == "Welcome Sem Conta !!"
    assert account_page.pegar_texto_aviso_sem_conta() == "Please open an account with us."
    assert account_page.operacoes_bancarias_visiveis() == []
