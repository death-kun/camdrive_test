import time

class CD_120:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.login_autotest()
        time.sleep(4)
        self.click_camera_CD_120()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD120_D521()
        self.app.logout_butten()

    def click_camera_CD_120(self):
        driver = self.app.driver
        self.click_CD_120 = driver.find_element_by_xpath('//*[@id="node_4343"]/a')
        self.click_CD_120.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD120_D521(self):
        self.app.Monitoring.archive_check()