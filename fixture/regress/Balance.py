import requests

class balance:

    def __init__(self, app):
        self.app = app

    def request_balance(self):
        data = {'username': 'autotest', 'password': 'autotest'}
        d = {'controller':'online', 'config':'{"balance":true,"tree":true,"check_camera_public_payment":false,"cameras":false}'}
        url1 = 'https://test.camdrive.org/'
        url2 = 'https://test.camdrive.org/state'

        s = requests.Session()   #Создание сеанс
        a = s.post(url1, data=data)     #Авторизация запросом
        c = a.cookies.get_dict()  #Получаем куки
        r = s.post(url=url2, data=d, cookies=c)   #Отправка запроса на получение баланса

        r2 = r.text
        print(c)
        print(r2)
        print(r.url)

        parsing1 = r2.split('],')[1]
        parsing2 = parsing1.split('<span')[0]
        self.parsing3 = parsing2.replace('"balance":"', '')
        print(self.parsing3, 'Баланс, который мы получаем запросом')

    def balance_gui(self):
        driver = self.app.driver
        pay_balance = driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td[1]/div/span')
        balance_attribute = pay_balance.get_attribute('textContent')
        self.parsing_balance_attribute = balance_attribute.replace('p', '')
        print(self.parsing_balance_attribute, 'Баланс, который отображается в ЛК')