import time

class CD320_AA06_ms3_dev:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.click_CD320_AA06_ms3_dev()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD320_AA06_ms3_dev()
        self.app.logout_butten()

    def click_CD320_AA06_ms3_dev(self):
        driver = self.app.driver
        self.click_CD320_AA06_ms3_dev = driver.find_element_by_xpath('//*[@id="node_12603"]/a').click()  # камера CD320(AA06)_ms3_dev
        self.click_CD320_AA06_ms3_dev.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD320_AA06_ms3_dev(self):
        self.app.Monitoring.archive_check()
