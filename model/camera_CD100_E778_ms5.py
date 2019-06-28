import time

class CD100_E778_ms5:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.click_camera_CD100_E778_ms5()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD100_E778_ms5()
        self.app.logout_butten()

    def click_camera_CD100_E778_ms5(self):
        driver = self.app.driver
        self.click_CD100_E778_ms5 = driver.find_element_by_xpath('//*[@id="node_6827"]/a').click()  # камера CD100(E778)_ms5_ПЗ
        self.click_CD100_E778_ms5.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD100_E778_ms5(self):
        self.app.Monitoring.archive_check()