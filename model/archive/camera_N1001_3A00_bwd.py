import time

class N1001_3A00_bwd:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.login_autotest()
        time.sleep(4)
        self.click_camera_N1001_3A00_bwd()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_N1001_3A00_bwd()
        self.app.logout_butten()

    def click_camera_N1001_3A00_bwd(self):
        driver = self.app.driver
        self.click_N1001_3A00_bwd = driver.find_element_by_xpath('//*[@id="node_14875"]/a').click()  # камера N1001(3A00)_bwd
        self.click_N1001_3A00_bwd.click()
        self.app.Monitoring.camera_title()

    def check_camera_N1001_3A00_bwd(self):
        self.app.Monitoring.archive_check()