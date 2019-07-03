from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class blocking:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        driver = self.app.driver
        self.app.open_home_page()
        i = 0
        while i != 6:
            self.app.Authorization.entering_the_wrong_password()
            driver.find_element_by_xpath('//input[@name="username"]').clear()
            driver.find_element_by_xpath('//input[@name="password"]').clear()
            i +=1
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p")))
            with open('entry block report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"Проверка Блокировки входа в личный кабинет" INFO: Проверка выполнена. Отобразилась надпись "Вход в личный кабинет заблокирован".\n')
                f.close()
            print('Проверка блокировки из-за неверно введенного пароля. Проверка прошла успешно. Блокировка произошла')
        except TimeoutException:
            with open('entry block error report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"Проверка Блокировки входа в личный кабинет" WARNING: Проверка провалилась. Надпись "Вход в личный кабинет заблокирован" не отобразилась.\n')
                f.close()
            print('Проверка блокировки из-за неверно введенного пароля. Проверка провалилась. Блокировка не произошла')