import time

class Local_RU:

    def __init__(self, app):
        self.app = app

    def local(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_css_selector('span.selected').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="login-box"]/div[1]/div/div/ul/li[1]').click()
        self.app.login_autotest()
