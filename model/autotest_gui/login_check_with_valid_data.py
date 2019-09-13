
class ValidData:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        driver = self.app.driver
        self.app.Authorization.open_home_page()
        self.app.Authorization.login_autotest()
        #Проверка того, что указан верный логин и пароль
        if driver.find_element_by_id('logo'):
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
        self.app.Authorization.logout_butten()