import time

class AuthorizationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        driver = self.app.driver
        driver.get('http://test.camdrive.org/')

    def login_autotest(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('autotest')
        driver.find_element_by_id('login').click()

    def site_opening(self):
        driver = self.app.driver
        driver.get('https://www.camdrive.com')

    def login_monitoring(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('service')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('7ujm6yhn')
        driver.find_element_by_id('login').click()
        time.sleep(1)

    def logout_butten(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[1]/td[2]/input').click()

    def login_with_incorrect_username(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('1')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('autotest')
        driver.find_element_by_id('login').click()

    def login_with_incorrect_password(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        driver.find_element_by_id('login').click()

    def password_visibility(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        driver.find_element_by_xpath('//div[@id="login-box"]/form/table/tbody/tr[2]/td[2]/div/div').click()
