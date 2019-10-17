import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DateDetermination:
    def __init__(self, app):
        self.app = app

    def find_yesterday(self):
        self.now = datetime.datetime.now()
        self.present_day = self.now.day
        self.strg_today = self.now.strftime('%B %d')
        self.yesterday = str(self.present_day - 1)

    def find_previous_month(self):
        today = datetime.date.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        self.yesterday = last_month.strftime('%d') #Определяем сколько дней в прошлем месяце
        print(self.yesterday)

    def determine_the_time(self):
        #Находим время для поиска архива, -12 часов от локального времени на рабочей станции
        now = datetime.datetime.now()
        present_hour = now.hour
        self.time_to_check = str(present_hour - 12)
        print(self.time_to_check, 'время, которое получаем после -12 часов от локального времени')
        if int(self.time_to_check) < 0:
            self.present_day = now.day
            self.time_to_check = 24 + int(self.time_to_check)
            print(self.time_to_check, 'время, которое мы получаем после')
            self.app.Monitoring.click_yesterday()
