import requests
import json

class RequestsCamdrive:

    def __init__(self, app):
        self.app = app

    def request_balance(self):

        DATA = {'controller':'online', 'config':'{"balance":true,"tree":true,"check_camera_public_payment":false,"cameras":false}'}
        URL = 'https://test.camdrive.org/state'

        request_balance = self.create_session.post(url=URL, data=DATA, cookies=self.receive_cookies_auth)  # Отправка запроса на получение баланса
        print(request_balance)
        print(request_balance.text)
        split_request_balance = request_balance.text.split('],')[1]
        split_request_balance_2 = split_request_balance.split('<span')[0]
        self.respon_balance = split_request_balance_2.replace('"balance":"', '')
        print(self.respon_balance, 'Баланс, который мы получаем запросом')

    def request_auth(self):

        DATA = {'username': 'autotest', 'password': 'autotest'}
        URL = 'https://test.camdrive.org/'

        self.create_session = requests.Session()  # Создание сеанс
        self.request_auth = self.create_session.post(URL, data=DATA)  # Авторизация запросом
        self.receive_cookies_auth = self.request_auth.cookies.get_dict()  # Получаем куки

    def request_online(self):

        DATA_AUTH = {'username': 'autotest', 'password': 'autotest'}
        DATA = {'action': 'screen_play', 'data': '{"num":1,"id":"cd2aec6529925a5632118fb0974a4a97"}'}
        URL_1 = 'https://test.camdrive.org/'
        # self.url2 = 'https://test.camdrive.org/camdrive/assets/flash/BewardVideoPlayerOnline_1.51.swf'  # плеер
        URL_2 = 'https://test.camdrive.org/online/get_screens_items'  # получить информацию по видео

        create_session = requests.Session()  # Создание сеанс
        request_auth = create_session.post(URL_1, data=DATA_AUTH)  # Авторизация запросом
        self.receive_cookies_auth = request_auth.cookies.get_dict()  # Получаем куки
        print(self.receive_cookies_auth)

        request_video = create_session.post(url=URL_2, data=DATA, cookies=self.receive_cookies_auth,
                                            headers={'Connection': 'close'})  # Отправка запроса на получение видео
        request_video2 = request_video.text
        create_session.close()
        print(request_video2)

        parsed_string = json.loads(request_video2)
        self.request_video3 = parsed_string['data']['1']['camera'][
            'connect_restriction']  # парсим json, чтобы получить результат connect_restriction
        print(self.request_video3)

    def request_call(self):
        PUSH_SERVER = "push-for-test.beward.ru"
        MAC = "186882304CDE"
        SIP_ADDRESS = "8_872_353"
        SIP_SERVER = "pbx.dev.ktotam.info"
        IP_ADDRESS = "192.168.28.159"
        LOGIN = "admin"
        PASSWORD = "admin"
        create_session = requests.Session()
        push = create_session.get(url='https://'+ PUSH_SERVER +'/intercom/?mac='+ MAC +'&event=0&mode=0&sipaddr1='+ SIP_ADDRESS +'@'+ SIP_SERVER +'')
        call = create_session.get(url='http://'+ LOGIN +':'+ PASSWORD +'@'+ IP_ADDRESS +'/cgi-bin/sip_cgi?action=call&Uri='+ SIP_ADDRESS +'@'+ SIP_SERVER +'')
        create_session.close()
        # print(push.headers)
        print(call.headers)

    def request_setting(self):
        DATA_AUTH = {'username': 'autotest', 'password': 'autotest'}
        URL_1 = 'https://test.camdrive.org'

        DATA = {'action': 'save', 'type': 'current', 'channel_id': 'cd2aec6529925a5632118fb0974a4a97', 'timezone': 'UP7', 'password': '',
                'password_confirm': '', 'mobile_audio': 0, 'device_audio_disabled': 0, 'lighting': 0, 'audio_input_gain': 28, 'frame_rate': 25,
                'resolution': 640*480, 'indication': 1, 'bitrate_limit': 0}

        DATA1 = {'action': 'content' , 'channel_id': 'cd2aec6529925a5632118fb0974a4a97', 'remember_tree': '{"node_id":"4184"}'}

        create_session = requests.Session()  # Создание сеанс
        request_auth = create_session.post(url=URL_1, data=DATA_AUTH)  # Авторизация запросом
        receive_cookies = request_auth.cookies.get_dict()  # Получаем куки
        request_setting = create_session.post(url='https://test.camdrive.org/settings/other/action', cookies=receive_cookies, data=DATA1)
        create_session.close()
        print(request_setting.text)

    # def request_test(self):
    #     driver = self.app.driver
    #     request_cookies_browser = driver.get_cookies()
    #     # print('cookies - ', request_cookies_browser)
    #
    #     split_cookies = str(request_cookies_browser).split("'httpOnly': False, ")[1]
    #     split_name = split_cookies.split(", 'path':")[0]
    #     # print(parsing_name, ' смотрим что осталось')
    #     split_value_1 = split_cookies.split("'secure': False, ")[1]
    #     split_value_2 = split_value_1.split('}]')[0]
    #     # print(parsing_value2, ' смотрим что осталось')
    #
    #     concatenation = split_name + ', ' + split_value_2
    #     print(concatenation)
    #
    #     create_session = requests.Session()
    #     cookies = dict(cookies_are=concatenation)
    #
    #     request_auth = create_session.post(url='https://test.camdrive.org', data= {'username': 'autotest', 'password': 'autotest'})
    #
    #     channel_id = self.app.Camera_List.chanel_id
    #     interval = self.app.LineHours.interval_value
    #     DATA = {'action': 'get_host', 'channel_id': channel_id, 'interval': interval}
    #
    #     request_archive = create_session.post(url='https://test.camdrive.org/archive', data= DATA, cookies=cookies)
    #     print(request_archive.text)
    #     create_session.close()
    #
    #     parsed_request_archive = json.loads(request_archive.text)
    #     print(parsed_request_archive)
