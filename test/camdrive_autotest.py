
def test_log_out(app):
    app.Authorization.login_with_incorrect_data()
    app.Authorization.password_visibility_check()
    app.Authorization.login_with_valid_data()

def test_forgot_your_password(app):
    app.forgot_your_password()
