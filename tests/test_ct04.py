def test_ct04_ordenar_clientes_pelo_primeiro_nome(login_page, manager_page, customers_page):
    login_page.logar_como_gerente_banco()
    manager_page.ir_para_clientes_tab()
    assert customers_page.esperar_pela_url(customers_page.URL)
    customers_page.esperar_quantidade_de_clientes(5)

    customers_page.ordenar_por_primeiro_nome()
    assert [cliente[0] for cliente in customers_page.pegar_clientes()] == [
        "Ron", "Neville", "Hermoine", "Harry", "Albus",
    ]

    customers_page.ordenar_por_primeiro_nome()
    assert [cliente[0] for cliente in customers_page.pegar_clientes()] == [
        "Albus", "Harry", "Hermoine", "Neville", "Ron",
    ]
