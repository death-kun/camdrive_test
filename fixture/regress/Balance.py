import request
import requests
import urllib.request
from httplib2 import Http
from urllib.parse import urlencode

class check_balance:

    def __init__(self, app):
        self.app = app

    def request(self):
        #Авторизация запросом
        data = {'username': 'autotest', 'password': 'autotest'}
        d = {'controller':'online', 'config':'{"balance":true,"tree":true,"check_camera_public_payment":false,"cameras":false}'}
        url1 = 'https://test.camdrive.org/'
        url2 = 'https://test.camdrive.org/state'

        s = requests.Session()
        e = s.post(url1, data=data)
        c = e.cookies.get_dict()
        r = s.post(url=url2, data=d, cookies=c)

        r2 = r.text
        print(c)
        print(r2)
        print(r.url)
        parsing1 = r2.split('],')[1]
        print(parsing1)


        # print(e.text)


        # r = urllib.request.urlopen('https://test.camdrive.org/state?action=get_state')
        # r = requests.post(url, auth=('autotest', 'autotest'))
        # print(r.text)
        # w = urllib.request.urlopen('https://test.camdrive.org/state')
        #
        # print(w.read().decode('utf-8'))
        # print(w.info().get('Data'))
        # print((w.getcode()))