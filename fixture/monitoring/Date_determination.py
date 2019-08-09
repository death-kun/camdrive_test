import datetime

class DateDetermination:
    def __init__(self, app):
        self.app = app

    def find_yesterday(self):
        self.now = datetime.datetime.now()
        cur_day = self.now.day
        self.strg_today = self.now.strftime('%B %d, %Y %H:%M')
        self.yesterday = str(cur_day - 1)

    def find_previous_month(self):
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        self.number_of_days = lastMonth.strftime('%d') #Определяем сколько дней в прошлем месяце
        print(self.number_of_days)