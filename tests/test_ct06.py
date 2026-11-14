class TestCT06:

    def test_ct06_Movimentar_somente_a_conta_selecionada(self, login_page, customers_page):
        login_page.logar_como_usuario_cliente("2")

        # Passo 1:
        customers_page.seleciona_conta_cliente("1004")

        dados_conta = customers_page.pegar_informacoes_conta()

        assert dados_conta['numero_conta'] == "1004"
        assert dados_conta['balanco'] == "0"
        assert dados_conta['moeda'] == "Dollar"   

        customers_page.seleciona_conta_cliente("1005")

        dados_conta = customers_page.pegar_informacoes_conta()

        assert dados_conta['numero_conta'] == "1005"
        assert dados_conta['balanco'] == "0"
        assert dados_conta['moeda'] == "Pound"         

        customers_page.seleciona_conta_cliente("1006")

        dados_conta = customers_page.pegar_informacoes_conta()

        assert dados_conta['numero_conta'] == "1006"
        assert dados_conta['balanco'] == "0"
        assert dados_conta['moeda'] == "Rupee"

        # Passo 2:
        customers_page.seleciona_conta_cliente("1005")
        # Passo 3:
        assert customers_page.depositar_valor_em_conta("300"), "Valor não depositado"

        # Passo 4:
        customers_page.seleciona_conta_cliente("1004")
        dados_conta = customers_page.pegar_informacoes_conta()
        assert dados_conta['balanco'] == "0"

        customers_page.seleciona_conta_cliente("1006")
        dados_conta = customers_page.pegar_informacoes_conta()
        assert dados_conta['balanco'] == "0"
