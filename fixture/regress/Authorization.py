import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class AuthorizationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        driver = self.app.driver
        driver.get('https://test.camdrive.org/')

    def authorization_with_login_autotest(self):
        driver = self.app.driver
        self.login_autotest()
        # Проверка того, что указан верный логин и пароль
        try:
            driver.find_element_by_id('logo')
            self.app.MessagesForTheReport.authorization_was_successful()
        except NoSuchElementException:
            self.app.MessagesForTheReport.authorization_failed()

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
        self.authorization_with_invalid_username()
        # Проверка того, что указан не верный логин
        try:
            error_notification = driver.find_element_by_xpath('//*[@id="login-box"]/div[2]').text
            if 'Ошибка идентификации. Проверьте правильность логина и введите Ваш пароль еще раз.' in error_notification:
               self.app.MessagesForTheReport.incorrect_login_entered()
        except TimeoutException:
            self.app.MessagesForTheReport.correct_login_entered()

    def login_with_incorrect_password(self):
        driver = self.app.driver
        self.authorization_with_invalid_password()
        #Проверка того, что указан не верный пароль
        try:
            error_notification = driver.find_element_by_xpath('//*[@id="login-box"]/div[2]').text
            if 'Ошибка идентификации. Проверьте правильность логина и введите Ваш пароль еще раз.' in error_notification:
                self.app.MessagesForTheReport.incorrect_password_entered()
        except TimeoutException:
            self.app.MessagesForTheReport.correct_password_entered()

    def blocking_account(self):
        driver = self.app.driver
        i = 0
        while i < 5:
            driver.find_element_by_xpath('//input[@name="username"]').clear()
            driver.find_element_by_xpath('//input[@name="password"]').clear()
            self.authorization_with_invalid_password()
            i+=1
        error_notification = driver.find_element_by_xpath('//*[@id="login-box"]/div[2]').text
        self.login_autotest()
        if 'Вход в личный кабинет заблокирован. Вы превысили максимальное количество попыток авторизации. Повторите через 15 мин.' in error_notification:
            self.app.MessagesForTheReport.login_blocked()
        else:
            self.app.MessagesForTheReport.no_lock_occurred()

    def authorization_with_invalid_password(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        driver.find_element_by_id('login').click()

    def authorization_with_invalid_username(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('1')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('autotest')
        driver.find_element_by_id('login').click()

    def password_visibility(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        driver.find_element_by_xpath('//div[@id="login-box"]/form/table/tbody/tr[2]/td[2]/div/div').click()
