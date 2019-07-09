import time

class CD120_D521_online:

    def __init__(self, app):
        self.app = app

    def detection_of_online(self):
        self.app.open_home_page()
        self.app.login_autotest()
        self.app.Camera_List.click_camera_CD120_D521()
        self.app.Online.online_gui()
        self.app.Online.request_online()
        # time.sleep(10)

