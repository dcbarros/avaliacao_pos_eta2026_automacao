def test_ct02_abrir_conta_para_um_cliente(app, login_page,manager_page, customers_page):
    login_page.open()
    login_page.logar_como_gerente_banco()
    app.manager_page.ir_para_abrir_account_tab()

    open_account_page = app.open_account_page

    # Passo 2: verificar a URL da página
    assert open_account_page.esperar_pela_url(open_account_page.URL)

    # Passos 3 e 4: selecionar cliente e moeda e clicar em Process
    open_account_page.selecionar_cliente("Harry Potter")
    open_account_page.selecionar_moeda("Dollar")
    open_account_page.clicar_em_process()

    # Passo 5: ler e fechar o alerta (o número é 1016 em um navegador novo)
    mensagem = open_account_page.pegar_texto_do_alerta()
    open_account_page.confirmar_alerta()

    assert mensagem.startswith("Account created successfully with account Number :")
    numero_conta = mensagem.split(":")[-1].strip()
    assert numero_conta.isdigit(), f"O alerta não trouxe um número de conta: {mensagem}"

    # Passo 6: em Customers, a conta nova aparece junto das contas de Harry Potter
    manager_page.ir_para_clientes_tab()
    assert customers_page.pegar_contas_do_cliente("Harry", "Potter") == ["1004", "1005", "1006", numero_conta]
