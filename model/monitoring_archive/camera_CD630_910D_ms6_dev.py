import time

class CD630_910D_ms6_dev:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.site_opening()
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.app.Camera_List.click_camera_CD630_910D_ms6_dev()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD630_910D_ms6_dev()
        self.app.Authorization.logout_butten()

    def check_camera_CD630_910D_ms6_dev(self):
        self.app.Monitoring.archive_check()