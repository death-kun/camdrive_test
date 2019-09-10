import time

class CD320_AA06_ms3_dev:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Authorization.site_opening()
        self.app.Authorization.login_monitoring()
        self.app.Camera_List.click_CD320_AA06_ms3_dev()
        self.app.Delete_TXT_files.delete_txt()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.app.Monitoring.archive_check()
        self.app.Authorization.logout_butten()