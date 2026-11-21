def test_ct13_voltar_tela_inicial_com_home(app, login_page, account_page):
    login_page.open()
    login_page.logar_como_usuario_cliente("2")

    assert account_page.validar_url_conta()

    account_page.clicar_home()

    assert login_page.esperar_pela_url(login_page.URL)
    assert login_page.encontrar_elemento(login_page.CUSTOMER_LOGIN_BUTTON).is_displayed()
    assert login_page.encontrar_elemento(login_page.MANAGER_LOGIN_BUTTON).is_displayed()
