def test_ct04_ordenar_clientes_pelo_primeiro_nome(login_page, manager_page, customers_page):
    # Pré-condições: área do gerente e lista de clientes abertas
    login_page.logar_como_gerente_banco()
    manager_page.ir_para_clientes_tab()
    assert customers_page.esperar_pela_url(customers_page.URL)
    customers_page.esperar_quantidade_de_clientes(5)

    # Passos 1 e 2: primeiro clique em First Name ordena de Z a A
    customers_page.ordenar_por_primeiro_nome()
    assert customers_page.pegar_primeiros_nomes() == [
        "Ron", "Neville", "Hermoine", "Harry", "Albus"
    ]

    # Passos 3 e 4: segundo clique inverte para A a Z
    customers_page.ordenar_por_primeiro_nome()
    assert customers_page.pegar_primeiros_nomes() == [
        "Albus", "Harry", "Hermoine", "Neville", "Ron"
    ]
