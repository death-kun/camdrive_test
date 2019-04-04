
def test_log_out(app):
    app.login_with_incorrect_data()
    app.password_visibility_check()
    app.login_with_valid_data()
