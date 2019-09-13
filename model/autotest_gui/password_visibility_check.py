
class PasswordVisibility:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        driver = self.app.driver
        self.app.Authorization.password_visibility()
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