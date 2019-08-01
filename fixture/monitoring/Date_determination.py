import datetime

class DateDetermination:
    def __init__(self, app):
        self.app = app

    def find_yesterday(self):
        self.now = datetime.datetime.now()
        cur_day = self.now.day
        self.strg_today = self.now.strftime('%B %d, %Y %H:%M')
        self.yesterday = str(cur_day - 1)