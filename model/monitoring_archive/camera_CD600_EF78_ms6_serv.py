import time

class CD600_EF78_ms6_serv:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.site_opening()
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.app.Camera_List.click_CD600_EF78_ms6_serv()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD600_EF78_ms6_serv()
        self.app.Authorization.logout_butten()

    def check_camera_CD600_EF78_ms6_serv(self):
        self.app.Monitoring.archive_check()