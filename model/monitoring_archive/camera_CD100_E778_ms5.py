import time

class CD100_E778_ms5:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.app.Camera_List.click_camera_CD100_E778_ms5()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD100_E778_ms5()
        self.app.logout_butten()

    def check_camera_CD100_E778_ms5(self):
        self.app.Monitoring.archive_check()