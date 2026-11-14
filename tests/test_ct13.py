def test_ct13_voltar_tela_inicial_com_home(app):
    app.login_page.open()
    app.login_page.logar_como_usuario_cliente("2")

    assert app.account_page.validar_url_conta()

    app.account_page.clicar_home()

    assert app.login_page.esperar_pela_url(app.login_page.URL)
    assert app.login_page.encontrar_elemento(app.login_page.CUSTOMER_LOGIN_BUTTON).is_displayed()
    assert app.login_page.encontrar_elemento(app.login_page.MANAGER_LOGIN_BUTTON).is_displayed()
