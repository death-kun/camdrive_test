import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class checkonlune:

    def __init__(self, app):
        self.app = app

    def online_screenshot(self):
        driver = self.app.driver
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="flash_1"]')))  #'//*[@id="screens"]/div[1]/div/div[2]/div[1]'  для отладки
            i = 0
            old_screenshot_player = 0
            while i < 300: # 5 минут в течение, которых проверяется стабильность онлайна
                driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]/div[1]').screenshot("1.png") #делаем скриншот видеоплеера
                self.app.RMS.computation_rms()

                if self.app.RMS.screenshot_player == old_screenshot_player:
                    print('Не идет онлайн')
                elif self.app.RMS.rms < 15.0:
                    print('Отображается серверное сообщение "Превышено максимальное допустимое количество одновременных подключений".')
                elif self.app.RMS.rms2 < 6.0:
                    print('Отображается ПРОГРЕССБАР')
                elif self.app.RMS.rms3 == 0.0:
                    print('Отображатеся серверное сообщение "Камера не подключена к серверу')
                else:
                    print('Идет онлайн')
                time.sleep(1)
                old_screenshot_player = self.app.RMS.screenshot_player
                i += 1
        except TimeoutException:
            print('Не загрузилось видео')


