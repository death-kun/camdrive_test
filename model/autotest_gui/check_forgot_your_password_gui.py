
class ForgotYourPassword:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        self.app.DeleteTxtFiles.delete_txt()
        self.app.DateDetermination.find_yesterday()
        self.app.Authorization.open_home_page()
        self.app.Authorization.open_form_forgot_yout_password()
