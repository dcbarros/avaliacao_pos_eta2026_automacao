def test_ct01_Cadastrar_Novo_cliente(app, login_page):
    login_page.open()
    login_page.logar_como_gerente_banco()
    app.manager_page.ir_para_add_customer_tab()
    app.add_customer_page.adicionar_customer("Aluno", "QA", "50000")

    # A mensagem é um alert nativo do navegador, não um elemento da página
    mensagem = app.add_customer_page.pegar_texto_do_alerta()
    app.add_customer_page.confirmar_alerta()

    # O id do cliente muda a cada cadastro, então validamos só o trecho fixo
    assert "Customer added successfully with customer id" in mensagem