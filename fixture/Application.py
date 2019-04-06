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
        #Проверка того, что указан не вернный пароль
        if driver.find_element_by_xpath('//div[@id="login-box"]/div[2]/span/p').text == "Ошибка идентификации. Проверьте правильность логина и введите Ваш пароль еще раз. Количество попыток ограничено!.":
            print('Проверка того, что указан не вернный пароль. Проверка прошла успешно. Введен некорректный пароль')
        else:
            print('Проверка того, что указан не вернный пароль. Проверка провалилась. Введены корректные значения')

    def password_visibility_check(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="login-box"]/form/table/tbody/tr[2]/td[2]/div/div').click()
        #Проверка, что при нажатии на "глаз" видно введенный пароль
        if driver.find_element_by_xpath('//input[@name="password"]').get_attribute('value') == "111":
            print('Проверка, что при нажатии на "глаз" видно введенный пароль. ППроверка прошла успешно. Пароль - 111')
        else:
            print('Проверка, что при нажатии на "глаз" видно введенный пароль. Проверка провалилась. Пароль не видно')

    def login_with_valid_data(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('autotest')
        driver.find_element_by_id('login').click()
        time.sleep(1)
        #Проверка того, что указан вернный логин и пароль
        if driver.find_element_by_xpath('//div[@id="title"]/div').get_attribute('value') == "Онлайн":
            print('Проверка того, что указан вернный логин и пароль. Проверка прошла успешно. Логин и пароль введены корректно')
        else:
            print('Проверка того, что указан вернный логин и пароль. Данные введены некорректно')


    def Stop(self):
        self.driver.quit()
