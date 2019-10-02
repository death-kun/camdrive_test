
class CheckTopEditButtons:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        self.app.Authorization.open_home_page()
        self.app.Authorization.login_autotest()
        self.app.CameraList.click_camera_CD120_D521()
        self.app.DeleteTxtFiles.delete_txt()
        self.app.DateDetermination.find_yesterday()
        self.app.TopEditButtons.add_camera_player1()
        self.app.TopEditButtons.add_camera_player2()
        self.app.TopEditButtons.add_camera_player3()
        self.app.TopEditButtons.add_camera_player4()
        self.app.TopEditButtons.add_camera_button()
        self.app.TopEditButtons.camera_rename_button()
        self.app.TopEditButtons.remove_camera_button()
        self.app.Authorization.logout_butten()