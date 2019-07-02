import time

class CD120_D521_online:

    def __init__(self, app):
        self.app = app

    def detection_of_online(self):
        self.app.login_autotest()
        time.sleep(4)
        self.app.Camera_List.click_camera_CD120_D521()


