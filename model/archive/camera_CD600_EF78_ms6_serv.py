import time

class CD600_EF78_ms6_serv:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.app.Monitoring.login_monitoring()
        time.sleep(4)
        self.click_CD600_EF78_ms6_serv()
        self.app.Monitoring.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD600_EF78_ms6_serv()
        self.app.logout_butten()

    def click_CD600_EF78_ms6_serv(self):
        driver = self.app.driver
        self.click_CD600_EF78_ms6_serv = driver.find_element_by_xpath('//*[@id="node_12601"]/a').click()  # камера CD600(EF78)_ms6_serv
        self.click_CD600_EF78_ms6_serv.click()
        self.app.Monitoring.camera_title()

    def check_camera_CD600_EF78_ms6_serv(self):
        self.app.Monitoring.archive_check()