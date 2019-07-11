
class CD120_D521_online:

    def __init__(self, app):
        self.app = app

    def detection_of_online(self):
        self.app.Authorization.open_home_page()
        self.app.Authorization.login_autotest()
        self.app.Camera_List.click_camera_CD120_D521()
        self.app.Player.add_camera_player1()
        self.app.Online.online_screenshot()
        self.app.Authorization.logout_butten()


