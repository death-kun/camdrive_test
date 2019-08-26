from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import math
import operator
from functools import reduce

class rms:

    def __init__(self, app):
        self.app = app

    def computation_rms(self):
        screenshot_error = Image.open("screenshots/error_code_0.png")  # скриншот с серверной ошибки Превышено максимальное подключение

        screenshot_progress_bar = Image.open("screenshots/progress_bar.png")  # скриншот с прогрессбаром

        screenshot_error_code_1 = Image.open("screenshots/error_code_1.png")  # скриншот с серверной ошибки  Камера не подключена к серверу

        self.screenshot_player = Image.open("1.png") # скриншот плеера

        # Среднеквадратическая разница. Чтобы измерить, насколько похожи два изображения, вы можете рассчитать среднеквадратичное (RMS) значение разницы между изображениями.
        # Если изображения абсолютно идентичны, это значение равно нулю.
        # Следующая функция использует функцию разности , а затем вычисляет среднеквадратичное значение по гистограмме полученного изображения
        h1 = self.screenshot_player.histogram()
        h2 = screenshot_error.histogram()
        h3 = screenshot_progress_bar.histogram()
        h4 = screenshot_error_code_1.histogram()

        self.rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))  # определяем разницу между скриншотом плеера и скриншотом серверной ошибки
        print(self.rms, ' сравнение с ошибкой')

        self.rms2 = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h3)) / len(h1))  # определяем разницу между скриншотом плеера и скриншотом прогрессбара
        print(self.rms2, ' сравнение с прогрессбаром')

        self.rms3 = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h4)) / len(h1))  # определеняем разницу между скринщотом плеера с скриншотом ошибки  камера не подключена к серверу
        print(self.rms3, ' сравнение с ошибкой камера не подключена к серверу')