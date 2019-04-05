from selenium import webdriver
import time



class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('D:\python test\camdrive_test\chromedriver.exe')
        driver = self.driver
        driver.delete_all_cookies()

    def open_home_page(self):
        driver = self.driver
        driver.get('http://test.camdrive.org/')

    def login_with_incorrect_data(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        driver.find_element_by_id('login').click()
        time.sleep(1)
        warning = driver.find_element_by_xpath('//div[@id="login-box"]/div[2]/span/p')
        # Проверка того, что указан не вернный пароль
        if not warning:
            raise AssertionError('Введены корректные значения')

    def password_visibility_check(self):
        driver = self.driver
        self.open_home_page()
        entry_field = driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        time.sleep(1)
        eye = driver.find_element_by_xpath('//div[@id="login-box"]/form/table/tbody/tr[2]/td[2]/div/div').click()

        # if entry_field.get_attribute('111'):
        #     print('Указан пароль 111')
        # else:
        #     print('Пароль скрыт')



    def login_with_valid_data(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('autotest')
        driver.find_element_by_id('login').click()
        time.sleep(1)
        # Проверка того, что указан вернный пароль
        if driver.find_element_by_xpath('//div[@id="title"]/div').is_displayed():
            print('Пароль введен корректно')


    def Stop(self):
        self.driver.quit()
