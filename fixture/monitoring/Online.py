from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import time
import math, operator
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
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="flash_1"]')))
            i = 0
            p1 = 0
            while i < 300: # 5 минут в течение, которых проверяется стабильность онлайна
                driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]/div').screenshot("1.png") #делаем скриншот видеоплеера
                screenshot_error = Image.open("D:/python test/camdrive_test/test/error_code_0.png") #скриншот с ошибкой
                screenshot_progress_bar = Image.open("D:/python test/camdrive_test/test/progress_bar.png") #скриншот с прогрессбаром
                self.p = Image.open("1.png")

                # Среднеквадратическая разница. Чтобы измерить, насколько похожи два изображения, вы можете рассчитать среднеквадратичное (RMS) значение разницы между изображениями.
                # Если изображения абсолютно идентичны, это значение равно нулю.
                # Следующая функция использует функцию разности , а затем вычисляет среднеквадратичное значение по гистограмме полученного изображения
                h1 = self.p.histogram()
                h2 = screenshot_error.histogram()
                rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1)) #определяем разницу между скриншотом плеера и скриншотом серверной ошибки
                print(rms, ' сравнение с ошибкой')

                h3 = screenshot_progress_bar.histogram()
                rms2 = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h3)) / len(h1)) #определяем разницу между скриншотом плеера и скриншотом прогрессбара
                print(rms2, ' сравнение с прогрессбаром')

                if self.p == p1:
                    print('не идет онлайн')
                elif rms < 15.0:
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!серверное сообщение')
                elif rms2 < 6.0:
                    print('!!!!!!!!!!ПРОГРЕССБАР!!!!!!!!!!!!!')
                else:
                    print('онлайн идет')
                time.sleep(1)
                p1 = self.p
                i += 1

        except TimeoutException:
            print('не загрузился плеер')
