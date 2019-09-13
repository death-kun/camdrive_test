from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class InvalidPassword:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        driver = self.app.driver
        self.app.Authorization.login_with_incorrect_password()
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
