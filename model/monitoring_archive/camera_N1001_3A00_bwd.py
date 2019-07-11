import time

class N1001_3A00_bwd:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.login_autotest()
        time.sleep(4)
        self.app.Camera_List.click_camera_N1001_3A00_bwd()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_N1001_3A00_bwd()
        self.app.Authorization.logout_butten()

    def check_camera_N1001_3A00_bwd(self):
        self.app.Monitoring.archive_check()