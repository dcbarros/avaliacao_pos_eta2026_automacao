def test_ct07_depositar_valor_na_conta(login_page, customers_page):
    login_page.logar_como_usuario_cliente("2")
    
    customers_page.seleciona_conta_cliente("1004")
    dados_conta = customers_page.pegar_informacoes_conta()

    assert dados_conta['numero_conta'] == "1004"
    assert dados_conta['balanco'] == "0"
    assert dados_conta['moeda'] == "Dollar"

    assert customers_page.depositar_valor_em_conta("500"), "Valor não depositado"
    assert customers_page.pegar_informacoes_input_amount() == ''
    assert customers_page.pegar_url() == "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
