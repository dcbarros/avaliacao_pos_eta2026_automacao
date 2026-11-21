def test_ct03_pesquisa_filtra_clientes_por_qualquer_coluna(login_page,manager_page, customers_page):
    # Pré-condição: área do gerente aberta
    login_page.open()
    login_page.logar_como_gerente_banco()

    # Passos 1 e 2: abrir Customers e verificar a URL
    manager_page.ir_para_clientes_tab()
    assert customers_page.esperar_pela_url(customers_page.URL)

    customers_page.esperar_quantidade_de_clientes(5)
    clientes_iniciais = customers_page.pegar_clientes()

    # Passo 3: pesquisar E55 (o texto só existe no Post Code desses dois clientes)
    customers_page.pesquisar("E55")
    customers_page.esperar_quantidade_de_clientes(2)
    assert sorted(customers_page.pegar_clientes()) == sorted([
        ("Ron", "Weasly", "E55555"),
        ("Albus", "Dumbledore", "E55656"),
    ])

    # Passo 4: apagar a pesquisa e conferir que os mesmos 5 clientes voltaram
    customers_page.limpar_pesquisa()
    customers_page.esperar_quantidade_de_clientes(5)
    assert customers_page.pegar_clientes() == clientes_iniciais
