import time

class CD120_D521_online:

    def __init__(self, app):
        self.app = app

    def detection_of_online(self):
        self.app.login_autotest()
        time.sleep(4)
        self.click_camera_CD120_D521()


    def click_camera_CD120_D521(self):
        driver = self.app.driver
        self.click_CD120_D521 = driver.find_element_by_xpath('//*[@id="node_4184"]/a')
        self.click_CD120_D521.click()
        self.app.Monitoring.camera_title()