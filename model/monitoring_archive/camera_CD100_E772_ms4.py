import time

class CD100_E772_ms4:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.app.Camera_List.click_camera_CD100_E772_ms4()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD100_E772_ms4()
        self.app.Authorization.logout_butten()

    def check_camera_CD100_E772_ms4(self):
        self.app.Monitoring.archive_check()