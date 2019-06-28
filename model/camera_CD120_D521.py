import time

class CD120_D521:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.delete_txt()
        self.app.login_autotest()
        time.sleep(4)
        self.click_CD120_D521()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD120_D521()
        self.app.logout_butten()

    def click_CD120_D521(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_4184"]/a').click()
        self.app.Monitoring.camera_title()

    def check_camera_CD120_D521(self):
        self.app.Monitoring.archive_check()