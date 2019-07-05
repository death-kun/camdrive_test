import requests
import json
import ast

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

        s = requests.Session()  # Создание сеанс
        a = s.post(url1, data=data)  # Авторизация запросом
        c = a.cookies.get_dict()  # Получаем куки
        print(c)

        r = s.post(url=url3, data=d, cookies=c)  # Отправка запроса на получение баланса
        r2 = r.text
        print(r2)
        
        parsed_string = json.loads(r2)
        r3 = parsed_string['data']['1']['camera']['connect_restriction'] #парсим json, чтобы получить результат connect_restriction
        print(r3)

