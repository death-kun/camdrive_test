
class downloadarchive:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        self.app.login_autotest()
        self.app.Camera_List.click_camera_CD_120()
        self.app.Archive.open_archive()
        self.app.Archive.download_archive()
        self.app.logout_butten()
