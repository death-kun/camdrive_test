from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import time
import math
import operator
from functools import reduce
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
                driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]/div').screenshot("1.png") #делаем скриншот видеоплеера
                screenshot_error = Image.open("error_code_0.png") #скриншот с серверной ошибки Превышено максимальное подключение
                screenshot_progress_bar = Image.open("progress_bar.png") #скриншот с прогрессбаром
                screenshot_error_code_1 = Image.open("error_code_1.png") #скриншот с серверной ошибки  Камера не подключена к серверу
                self.screenshot_player = Image.open("1.png")

                # Среднеквадратическая разница. Чтобы измерить, насколько похожи два изображения, вы можете рассчитать среднеквадратичное (RMS) значение разницы между изображениями.
                # Если изображения абсолютно идентичны, это значение равно нулю.
                # Следующая функция использует функцию разности , а затем вычисляет среднеквадратичное значение по гистограмме полученного изображения
                h1 = self.screenshot_player.histogram()
                h2 = screenshot_error.histogram()
                rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1)) #определяем разницу между скриншотом плеера и скриншотом серверной ошибки
                print(rms, ' сравнение с ошибкой')

                h3 = screenshot_progress_bar.histogram()
                rms2 = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h3)) / len(h1)) #определяем разницу между скриншотом плеера и скриншотом прогрессбара
                print(rms2, ' сравнение с прогрессбаром')

                h4 = screenshot_error_code_1.histogram()
                rms3 = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h4)) / len(h1)) #определеняем разницу между скринщотом плеера с скриншотом ошибки  камера не подключена к серверу
                print(rms3, ' сравнение с ошибкой камера не подключена к серверу')

                if self.screenshot_player == old_screenshot_player:
                    print('Не идет онлайн')
                elif rms < 15.0:
                    print('Отображается серверное сообщение "Превышено максимальное допустимое количество одновременных подключений".')
                elif rms2 < 6.0:
                    print('Отображается ПРОГРЕССБАР')
                elif rms3 == 0.0:
                    print('Отображатеся серверное сообщение "Камера не подключена к серверу')
                else:
                    print('Идет онлайн')
                time.sleep(1)
                old_screenshot_player = self.screenshot_player
                i += 1

        except TimeoutException:
            print('Не загрузилось видео')
