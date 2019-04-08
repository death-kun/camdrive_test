
def test_log_out(app):
    app.Authorization.login_with_incorrect_data() #Проверка того, что указан не верный пароль
    app.Authorization.password_visibility_check() #Проверка, что при нажатии на "глаз" видно введенный пароль
    app.Authorization.login_with_valid_data() #Проверка того, что указан верный логин и пароль

def test_forgot_your_password(app):
    app.forgot_your_password() #Проверка перехода на форму "Забыли пароль?"

def test_checkbox(app):
    app.tick_activity() #Проверка активности "галочки"