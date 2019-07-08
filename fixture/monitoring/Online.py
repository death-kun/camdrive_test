import requests
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class checkonlune:

    def __init__(self, app):
        self.app = app

    def request_online(self):

        data = {'username': 'autotest', 'password': 'autotest'}
        d = {'action': 'screen_play', 'data': '{"num":1,"id":"cd2aec6529925a5632118fb0974a4a97"}'}
        url1 = 'https://test.camdrive.org/'
        url2 = 'https://test.camdrive.org/camdrive/assets/flash/BewardVideoPlayerOnline_1.51.swf' #плеер
        url3 = 'https://test.camdrive.org/online/get_screens_items' #получить информацию по видео
        error_code = 'outOfRangeMaxConnectionsLimitTariff' #код серверной ошибки
        error_code_1 = 'deviceNotConnectedToServer'  #код ошибки что камера не подключена
        z = requests.Session()

        s = requests.Session()  # Создание сеанс
        a = s.post(url1, data=data)  # Авторизация запросом
        c = a.cookies.get_dict()  # Получаем куки
        print(c)

        request_video = s.post(url=url3, data=d, cookies=c, headers={'Connection':'close'}) # Отправка запроса на получение видео
        request_video2 = request_video.text
        s.close()
        print(request_video2)

        parsed_string = json.loads(request_video2)
        self.request_video3 = parsed_string['data']['1']['camera']['connect_restriction'] #парсим json, чтобы получить результат connect_restriction
        print(self.request_video3)

    def online_gui(self):
        driver = self.app.driver
        self.app.Player.add_camera_player1()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='screens']/div[1]/div/div[2]/div[1]")))
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]/div[1]/a').click() #клик по надписе загрузить flash
        time.sleep(5)

    def request_flash(self):
        driver = self.app.driver
        url1 = 'https://test.camdrive.org/'

        url2 = 'https://test.camdrive.org/online'
        d = {
            "profile.default_content_setting_values.plugins": 1,
                "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
                "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
                "profile.content_settings.exceptions.plugins.*,*.setting": 1,
                "DefaultPluginsSetting": 3,
                "PluginsAllowedForUrls":"https://test.camdrive.org:443"
                }
        # d = {'dismiss_count': 1, 'flash_data': 'https://test.camdrive.org:443', 'flashPreviouslyChanged': True}
        data = {'username': 'autotest', 'password': 'autotest'}

        # d = {'dismiss_count':1, 'flash_data':'https://test.camdrive.org:443', 'flashPreviouslyChanged':True}
        s = requests.Session()  # Создание сеанс
        a = s.post(url=url1, data=data)  # Авторизация запросо
        c = a.cookies.get_dict()  # Получаем куки
        driver.delete_all_cookies()

        request_video = s.post(url=url2, data=d, cookies=c) # Отправка запроса на получение видео

        print(request_video.text)
        print(request_video.url)
