import time

class CD_120:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Authorization.open_home_page()
        self.app.Authorization.login_autotest()
        self.app.CameraList.click_camera_CD_120()
        self.app.DeleteTxtFiles.delete_txt()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.app.Monitoring.archive_check()
        self.app.Authorization.logout_butten()