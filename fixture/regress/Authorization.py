import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class AuthorizationHelper:

    def __init__(self, app):
        self.app = app

    def login_with_incorrect_username(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('1')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('autotest')
        driver.find_element_by_id('login').click()
        #Проверка того, что указан не верный логин
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#text")))
            with open('authorization report.txt', 'a', encoding='utf-8') as f:
                f.write('"Проверка валидных/невалидных данных" INFO: Проверка выполнена. Отобразилась надпись "Ошибка идентификации".\n')
                f.close()
            print('Проверка того, что указан не верный пароль. Проверка прошла успешно. Введен некорректный логин')
        except TimeoutException:
            with open('authorization error report.txt', 'a', encoding='utf-8') as f:
                f.write('"Проверка валидных/невалидных данных" WARNING: Проверка провалилась. Надпись "Ошибка идентификации" не отобразилась.\n')
                f.close()
            print('Проверка того, что указан не верный пароль. Проверка провалилась. Введены корректные значения')


    def login_with_incorrect_password(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.entering_the_wrong_password()
        #Проверка того, что указан не верный пароль
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#text")))
            with open('authorization report.txt', 'a', encoding='utf-8') as f:
                f.write('"Проверка валидных/невалидных данных" INFO: Проверка выполнена. Отобразилась надпись "Ошибка идентификации".\n')
                f.close()
            print('Проверка того, что указан не верный пароль. Проверка прошла успешно. Введен некорректный пароль')
        except TimeoutException:
            with open('authorization error report.txt', 'a', encoding='utf-8') as f:
                f.write('"Проверка валидных/невалидных данных" WARNING: Проверка провалилась. Надпись "Ошибка идентификации" не отобразилась.\n')
                f.close()
            print('Проверка того, что указан не верный пароль. Проверка провалилась. Введены корректные значения')

    def entering_the_wrong_password(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        driver.find_element_by_id('login').click()

    def password_visibility_check(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('111')
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="login-box"]/form/table/tbody/tr[2]/td[2]/div/div').click()
        #Проверка, что при нажатии на "глаз" видно введенный пароль
        if driver.find_element_by_xpath('//input[@name="password"]').get_attribute('value') == "111":
            with open('authorization report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"Проверка скрытие/открытие пароля при нажатии на "глазок"" INFO: Проверка выполнена. Пароль отображается.\n')
                f.close()
            print('Проверка, что при нажатии на "глаз" видно введенный пароль. Проверка прошла успешно. Пароль - 111')
        else:
            with open('authorization error report.txt', 'a', encoding='utf-8') as f:
                f.write('"Проверка скрытие/открытие пароля при нажатии на "глазок"" WARNING: Проверка провалилась. Пароль не отображается.\n')
                f.close()
            print('Проверка, что при нажатии на "глаз" видно введенный пароль. Проверка провалилась. Пароль не видно')

    def login_with_valid_data(self):
        driver = self.app.driver
        self.app.login_autotest()
        #Проверка того, что указан верный логин и пароль
        if driver.find_element_by_id('logo'):
            self.app.logout_butten()
            with open('authorization report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"Проверка валидных/невалидных данных" INFO: Проверка выполнена. Авторизация прошла успешно.\n')
                f.close()
            print('Проверка того, что указан верный логин и пароль. Проверка прошла успешно. Логин и пароль введены корректно')
        else:
            with open('authorization error report.txt', 'a', encoding='utf-8') as f:
                f.write('"Проверка валидных/невалидных данных" WARNING: Проверка провалилась. Авторизация не произошла.\n')
                f.close()
            print('Проверка того, что указан верный логин и пароль. Проверка провалилась. Данные введены некорректно')

    def forgot_your_password_gui(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_link_text('Забыли пароль?').click()
        #Проверка перехода на форму "Забыли пароль?"
        if driver.find_element_by_css_selector('.info-title').text == "Восстановление пароля":
            print('Проверка перехода на форму "Забыли пароль?". Проверка прошла успешно. Открылась форма "Забыли пароль?".')
        else:
            print('Проверка перехода на форму "Забыли пароль?". Проверка провалилась. Форма "Забыли пароль?" не открылась.')
