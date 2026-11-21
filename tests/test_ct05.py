def test_ct05_excluir_cliente(login_page, manager_page, add_customer_page, customers_page):
    login_page.logar_como_gerente_banco()
    manager_page.ir_para_add_customer()
    add_customer_page.adicionar_cliente("Aluno", "QA", "50000")

    manager_page.ir_para_clientes_tab()
    assert customers_page.esperar_pela_url(customers_page.URL)
    customers_page.pesquisar("Aluno")
    customers_page.esperar_quantidade_de_clientes(1)
    assert customers_page.pegar_clientes() == [("Aluno", "QA", "50000")]

    customers_page.excluir_cliente_filtrado()
    assert customers_page.esperar_quantidade_de_clientes(0)
    assert customers_page.pegar_url() == customers_page.URL
