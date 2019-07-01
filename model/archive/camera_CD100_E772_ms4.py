import time

class CD100_E772_ms4:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.click_camera_CD100_E772_ms4()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD100_E772_ms4()
        self.app.logout_butten()

    def click_camera_CD100_E772_ms4(self):
        driver = self.app.driver
        self.click_CD100_E772_ms4 = driver.find_element_by_xpath('//*[@id="node_6830"]/a').click()  # камера CD100(E772)_ms4_ПЗ
        self.click_CD100_E772_ms4.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD100_E772_ms4(self):
        self.app.Monitoring.archive_check()