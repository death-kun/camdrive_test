import time

class CD310_2E51_ms4_dev:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.click_camera_CD310_2E51_ms4_dev()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD310_2E51_ms4_dev()
        self.app.logout_butten()

    def click_camera_CD310_2E51_ms4_dev(self):
        driver = self.app.driver
        self.click_CD310_2E51_ms4_dev = driver.find_element_by_xpath('//*[@id="node_13959"]/a').click()  # камера CD310(2E51)_ms4_dev
        self.click_CD310_2E51_ms4_dev.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD310_2E51_ms4_dev(self):
        self.app.Monitoring.archive_check()