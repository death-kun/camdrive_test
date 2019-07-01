def test_Log_In(app):
    app.Authorization.login_with_valid_data() #Проверка того, что указан верный логин и пароль
    app.Authorization.login_with_incorrect_password() #Проверка того, что указан не верный пароль
    app.Authorization.login_with_incorrect_username() #Проверка того, что указан не верный логин

def test_Eye(app):
    app.Authorization.password_visibility_check() #Проверка, что при нажатии на "глаз" видно введенный пароль

