import time

class MonitoringCD120_D521:

    def __init__(self, app):
        self.app = app

    def autotest_script(self):
        self.app.DeleteTxtFiles.delete_txt()
        self.app.DateDetermination.find_yesterday()
        self.app.Authorization.open_home_page()
        self.app.Authorization.login_with_incorrect_username()
        self.app.Authorization.login_with_incorrect_password()
        self.app.Authorization.authorization_with_login_autotest()
        self.app.CameraList.click_camera_CD120_D521()
        self.app.Monitoring.getting_schedule()
        time.sleep(4)
        self.app.Monitoring.definition_of_archive_time_period()
        self.app.Authorization.logout_butten()