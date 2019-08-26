import time

class CD600_EF78_ms6_serv:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Authorization.site_opening()
        self.app.Authorization.login_monitoring()
        self.app.Camera_List.click_CD600_EF78_ms6_serv()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.app.Monitoring.archive_check()
        self.app.Authorization.logout_butten()