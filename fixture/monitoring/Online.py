import requests


class checkonlune:

    def __init__(self, app):
        self.app = app

    def request_online(self):
        data = {'username': 'autotest', 'password': 'autotest'}
        d = {'action': 'screen_play', 'data': '{"num":1,"id":"cd2aec6529925a5632118fb0974a4a97"}'}
        url1 = 'https://test.camdrive.org/'
        url2 = 'https://test.camdrive.org/camdrive/assets/flash/BewardVideoPlayerOnline_1.51.swf' #плеер
        url3 = 'https://test.camdrive.org/online/get_screens_items'

        s = requests.Session()  # Создание сеанс
        a = s.post(url1, data=data)  # Авторизация запросом
        c = a.cookies.get_dict()  # Получаем куки
        r = s.post(url=url3, data=d, cookies=c)  # Отправка запроса на получение баланса

        r2 = r.text
        print(c)
        print(r2)
        print(r.url)
