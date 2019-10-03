
class CheckAuthorization:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        self.app.Authorization.open_home_page()
        self.app.DeleteTxtFiles.delete_txt()
        self.app.DateDetermination.find_yesterday()
        self.app.Authorization.authorization_with_login_autotest()
        self.app.Authorization.logout_butten()
        self.app.Authorization.login_with_incorrect_username()
        self.app.Authorization.login_with_incorrect_password()