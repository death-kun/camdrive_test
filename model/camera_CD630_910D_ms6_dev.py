import time

class CD630_910D_ms6_dev:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.click_camera_CD630_910D_ms6_dev()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD630_910D_ms6_dev()
        self.app.logout_butten()

    def click_camera_CD630_910D_ms6_dev(self):
        driver = self.app.driver
        self.click_CD630_910D_ms6_dev = driver.find_element_by_xpath('//*[@id="node_12602"]/a').click()  # камера CD630(910D)_ms6_dev
        self.click_CD630_910D_ms6_dev.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD630_910D_ms6_dev(self):
        self.app.Monitoring.archive_check()