import datetime
from selenium.webdriver.common.by import By


class schedule:

    def __init__(self, app):
        self.app = app

    def open_schedule(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="navigation"]/table/tbody/tr/td[3]/a').click()
        driver.find_element_by_xpath('//*[@id="subsections"]/table/tbody/tr/td[2]/a').click()

    def schedule_first_tree(self):
        self.app.check_first_tree()

    def schedule_second_tree(self):
        self.app.check_second_tree()

    def yesterday_day_of_the_week(self):
        driver = self.app.driver
        now = datetime.datetime.today().weekday()
        if now > 0:
            yesterday_weekday = now - 1
        else:
            yesterday_weekday = now
        #Циферное обозначение дней недели
        Mon = 0
        W = 1
        Wed = 2
        Th = 3
        Fri = 4
        Sat = 5
        Sun = 6

        if yesterday_weekday == Mon:
            self.monday()
        elif yesterday_weekday == W:
            self.tuesday()
        elif yesterday_weekday == Wed:
            self.wednesday()
        elif yesterday_weekday == Th:
            self.thursday()
        elif yesterday_weekday == Fri:
            self.friday()
        elif yesterday_weekday == Sat:
            self.saturday()
        elif yesterday_weekday == Sun:
            self.sunday()

    def sunday(self):
        driver = self.app.driver
        # Воскресенье
        Sunday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]')
        Sunday.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item"]')

    def saturday(self):
        driver = self.app.driver
        # Суббота
        Saturday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]')
        Saturday.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item"]')

    def friday(self):
        driver = self.app.driver
        # Пятница
        Friday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]')
        Friday.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item"]')

    def thursday(self):
        driver = self.app.driver
        # Четверг
        Thursday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]')
        Thursday.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item"]')

    def wednesday(self):
        driver = self.app.driver
        # Среда
        Wednesday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]')
        Wednesday.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item"]')

    def tuesday(self):
        driver = self.app.driver
        # Вторник
        Tuesday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]')
        Tuesday.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item"]')

    def monday(self):
        driver = self.app.driver
        # Понедельник
        Monday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]')
        massiv = []
        for i in range(0, 24, 1):
            self.item_T = Monday.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="item  button" or @class="item  detection" or @class="item  constant" or @class="item"]')[i]
            massiv.append(i)
        print(massiv)

    def items_schedule(self):
        driver = self.app.driver
        self.item1 = 1 # 1 = постоянная запись
        self.item2 = 2 # 2 = по нажатию
        self.item3 = 3 # 3 = по детекции
        self.item4 = 0 # 0 = нет записи


    def item_time0(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[2]')

        if driver.find_element(By.CSS_SELECTOR, 'td.item.constant'):
            self.element_time_0 = 1                                                         # 1 = постоянная запись
        elif driver.find_element(By.CSS_SELECTOR, 'td.item.button'):
            self.element_time_0 = 2                                                         # 2 = по нажатию
        elif driver.find_element(By.CSS_SELECTOR, 'td.item.detection'):
            self.element_time_0 = 3                                                         # 3 = по детекции
        elif driver.find_element(By.CSS_SELECTOR, 'td.item.empty'):
            self.element_time_0 = 0                                                         # 0 = нет записи
        return self.element_time_0

        # time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[2]')
        # time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[3]')
        # time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[4]')
        # time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[5]')
        # time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[6]')
        # time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[7]')
        # time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[8]')
        # time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[9]')
        # time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[10]')
        # time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[11]')
        # time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[12]')
        # time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[13]')
        # time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[14]')
        # time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[15]')
        # time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[16]')
        # time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[17]')
        # time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[18]')
        # time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[19]')
        # time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[20]')
        # time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[21]')
        # time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[22]')
        # time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[23]')
        # time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[24]')


