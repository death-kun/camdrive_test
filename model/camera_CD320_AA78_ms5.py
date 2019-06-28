import time

class CD320_AA78_ms5:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.click_camera_CD320_AA78_ms5()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD320_AA78_ms5()
        self.app.logout_butten()

    def click_camera_CD320_AA78_ms5(self):
        driver = self.app.driver
        self.click_CD320_AA78_ms5 = driver.find_element_by_xpath('//*[@id="node_11460"]/a').click()  # камера CD320(AA78)_ms5_Пр_С
        self.click_CD320_AA78_ms5.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD320_AA78_ms5(self):
        self.app.Monitoring.archive_check()