import requests
import json

class requests_camdrive:

    def __init__(self, app):
        self.app = app

    def request_balance(self):

        d = {'controller':'online', 'config':'{"balance":true,"tree":true,"check_camera_public_payment":false,"cameras":false}'}
        url = 'https://test.camdrive.org/state'

        r = self.s.post(url=url, data=d, cookies=self.c)  # Отправка запроса на получение баланса
        r2 = r.text

        parsing1 = r2.split('],')[1]
        parsing2 = parsing1.split('<span')[0]
        self.parsing3 = parsing2.replace('"balance":"', '')
        print(self.parsing3, 'Баланс, который мы получаем запросом')

    def request_auth(self):

        data = {'username': 'autotest', 'password': 'autotest'}
        url1 = 'https://test.camdrive.org/'

        self.s = requests.Session()  # Создание сеанс
        self.a = self.s.post(url1, data=data)  # Авторизация запросом
        self.c = self.a.cookies.get_dict()  # Получаем куки

    def request_online(self):

        data = {'username': 'autotest', 'password': 'autotest'}
        d = {'action': 'screen_play', 'data': '{"num":1,"id":"cd2aec6529925a5632118fb0974a4a97"}'}
        url1 = 'https://test.camdrive.org/'
        self.url2 = 'https://test.camdrive.org/camdrive/assets/flash/BewardVideoPlayerOnline_1.51.swf'  # плеер
        url3 = 'https://test.camdrive.org/online/get_screens_items'  # получить информацию по видео

        s = requests.Session()  # Создание сеанс
        a = s.post(url1, data=data)  # Авторизация запросом
        self.c = a.cookies.get_dict()  # Получаем куки
        print(self.c)

        request_video = s.post(url=url3, data=d, cookies=self.c,
                               headers={'Connection': 'close'})  # Отправка запроса на получение видео
        request_video2 = request_video.text
        s.close()
        print(request_video2)

        parsed_string = json.loads(request_video2)
        self.request_video3 = parsed_string['data']['1']['camera'][
            'connect_restriction']  # парсим json, чтобы получить результат connect_restriction
        print(self.request_video3)

    # def request_player(self):
    #
    #     s = requests.Session()
    #     r = s.get(url=self.url2, cookies=self.c, headers={"Accept": "*/*",
    #                                                     "Accept-Encoding": "gzip, deflate, br",
    #                                                     "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    #                                                     "Connection": "keep-alive",
    #                                                     "Referer": "https://test.camdrive.org/online",
    #                                                     "Host": "test.camdrive.org",
    #                                                     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    #                                                     "X-Requested-With": "ShockwaveFlash/32.0.0.207"})
    #     r2 = r.headers.items()
    #     s.close()
    #     # print(r2)

    def request_setting(self):
        data = {'username': 'autotest', 'password': 'autotest'}
        url1 = 'https://test.camdrive.org/'


        s = requests.Session()  # Создание сеанс
        a = s.post(url=url1, data=data)  # Авторизация запросом
        c = a.cookies.get_dict()  # Получаем куки
        r = s.post(url='https://test.camdrive.org/settings/other/action', cookies=c, data={"action": "content", "channel_id": "dbe81e3bd23e8f6b697b9b234784cc39dbe81e3bd23e8f6b697b9b234784cc39"})
        r2 = r.text
        s.close()
        print(r2)

    def request_test(self):

        d = {'action': 'get_host', 'channel_id': 'cd2aec6529925a5632118fb0974a4a97'}
        req = requests.post(url='https://test.camdrive.org/archive', data=d)
        print(req.text)
