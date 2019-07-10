from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class checkonlune:

    def __init__(self, app):
        self.app = app



    def online_gui(self):
        driver = self.app.driver
        self.app.Player.add_camera_player1()



