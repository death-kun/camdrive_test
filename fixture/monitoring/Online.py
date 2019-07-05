import requests
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class checkonlune:

    def __init__(self, app):
        self.app = app

    def request_online(self):

        data = {'username': 'autotest', 'password': 'autotest'}
        d = {'action': 'screen_play', 'data': '{"num":1,"id":"cd2aec6529925a5632118fb0974a4a97"}'}
        url1 = 'https://test.camdrive.org/'
        url2 = 'https://test.camdrive.org/camdrive/assets/flash/BewardVideoPlayerOnline_1.51.swf' #плеер
        url3 = 'https://test.camdrive.org/online/get_screens_items' #получить информацию по видео
        errore_code = 'outOfRangeMaxConnectionsLimitTariff' #код серверной ошибки
        errore_code_1 = 'deviceNotConnectedToServer'  #код ошибки что камера не подключена

        s = requests.Session()  # Создание сеанс
        a = s.post(url1, data=data)  # Авторизация запросом
        c = a.cookies.get_dict()  # Получаем куки
        print(c)

        request_video = s.post(url=url3, data=d, cookies=c)  # Отправка запроса на получение видео
        request_video2 = request_video.text
        print(request_video2)

        parsed_string = json.loads(request_video2)
        self.request_video3 = parsed_string['data']['1']['camera']['connect_restriction'] #парсим json, чтобы получить результат connect_restriction
        print(self.request_video3)

    def online_gui(self):
        driver = self.app.driver
        self.app.Player.add_camera_player1()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='screens']/div[1]/div/div[2]/div[1]")))
        driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]/div[1]/a').click() #клик по надписе загрузить flash
