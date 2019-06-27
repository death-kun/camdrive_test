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
            yesterday_weekday = now + 6
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
        time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[2]')
        if "item " in time_0.get_attribute("class"):
            self.element_time_0 = 0  # 0 = нет записи
        if "item detection" in time_0.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_0 = 1  # 1 = запись есть

        time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[3]')
        if "item " in time_1.get_attribute("class"):
            self.element_time_1 = 0  # 0 = нет записи
        if "item detection" in time_1.get_attribute("class"):
            self.element_time_1 = 2  # 2 = запись по детекции
        else:
            self.element_time_1 = 1  # 1 = запись есть

        time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[4]')
        if "item " in time_2.get_attribute("class"):
            self.element_time_2 = 0  # 0 = нет записи
        if "item detection" in time_2.get_attribute("class"):
            self.element_time_2 = 2  # 2 = запись по детекции
        else:
            self.element_time_2 = 1  # 1 = запись есть

        time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[5]')
        if "item " in time_3.get_attribute("class"):
            self.element_time_3 = 0  # 0 = нет записи
        if "item detection" in time_3.get_attribute("class"):
            self.element_time_3 = 2  # 2 = запись по детекции
        else:
            self.element_time_3 = 1  # 1 = запись есть

        time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[6]')
        if "item " in time_4.get_attribute("class"):
            self.element_time_4 = 0  # 0 = нет записи
        if "item detection" in time_4.get_attribute("class"):
            self.element_time_4 = 2  # 2 = запись по детекции
        else:
            self.element_time_4 = 1  # 1 = запись есть

        time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[7]')
        if "item " in time_5.get_attribute("class"):
            self.element_time_5 = 0  # 0 = нет записи
        if "item detection" in time_5.get_attribute("class"):
            self.element_time_5 = 2  # 2 = запись по детекции
        else:
            self.element_time_5 = 1  # 1 = запись есть

        time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[8]')
        if "item " in time_6.get_attribute("class"):
            self.element_time_6 = 0  # 0 = нет записи
        if "item detection" in time_6.get_attribute("class"):
            self.element_time_6 = 2  # 2 = запись по детекции
        else:
            self.element_time_6 = 1  # 1 = запись есть

        time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[9]')
        if "item " in time_7.get_attribute("class"):
            self.element_time_7 = 0  # 0 = нет записи
        if "item detection" in time_7.get_attribute("class"):
            self.element_time_7 = 2  # 2 = запись по детекции
        else:
            self.element_time_7 = 1  # 1 = запись есть

        time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[10]')
        if "item " in time_8.get_attribute("class"):
            self.element_time_8 = 0  # 0 = нет записи
        if "item detection" in time_8.get_attribute("class"):
            self.element_time_8 = 2  # 2 = запись по детекции
        else:
            self.element_time_8 = 1  # 1 = запись есть

        time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[11]')
        if "item " in time_9.get_attribute("class"):
            self.element_time_9 = 0  # 0 = нет записи
        if "item detection" in time_9.get_attribute("class"):
            self.element_time_9 = 2  # 2 = запись по детекции
        else:
            self.element_time_9 = 1  # 1 = запись есть

        time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[12]')
        if "item " in time_10.get_attribute("class"):
            self.element_time_10 = 0  # 0 = нет записи
        if "item detection" in time_10.get_attribute("class"):
            self.element_time_10 = 2  # 2 = запись по детекции
        else:
            self.element_time_10 = 1  # 1 = запись есть

        time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[13]')
        if "item " in time_11.get_attribute("class"):
            self.element_time_11 = 0  # 0 = нет записи
        if "item detection" in time_11.get_attribute("class"):
            self.element_time_11 = 2  # 2 = запись по детекции
        else:
            self.element_time_11 = 1  # 1 = запись есть

        time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[14]')
        if "item " in time_12.get_attribute("class"):
            self.element_time_12 = 0  # 0 = нет записи
        if "item detection" in time_12.get_attribute("class"):
            self.element_time_12 = 2  # 2 = запись по детекции
        else:
            self.element_time_12 = 1  # 1 = запись есть

        time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[15]')
        if "item " in time_13.get_attribute("class"):
            self.element_time_13 = 0  # 0 = нет записи
        if "item detection" in time_13.get_attribute("class"):
            self.element_time_13 = 2  # 2 = запись по детекции
        else:
            self.element_time_13 = 1  # 1 = запись есть

        time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[16]')
        if "item " in time_14.get_attribute("class"):
            self.element_time_14 = 0  # 0 = нет записи
        if "item detection" in time_14.get_attribute("class"):
            self.element_time_14 = 2  # 2 = запись по детекции
        else:
            self.element_time_14 = 1  # 1 = запись есть

        time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[17]')
        if "item " in time_15.get_attribute("class"):
            self.element_time_15 = 0  # 0 = нет записи
        if "item detection" in time_15.get_attribute("class"):
            self.element_time_15 = 2  # 2 = запись по детекции
        else:
            self.element_time_15 = 1  # 1 = запись есть

        time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[18]')
        if "item " in time_16.get_attribute("class"):
            self.element_time_16 = 0  # 0 = нет записи
        if "item detection" in time_16.get_attribute("class"):
            self.element_time_16 = 2  # 2 = запись по детекции
        else:
            self.element_time_16 = 1  # 1 = запись есть

        time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[19]')
        if "item " in time_17.get_attribute("class"):
            self.element_time_17 = 0  # 0 = нет записи
        if "item detection" in time_17.get_attribute("class"):
            self.element_time_17 = 2  # 2 = запись по детекции
        else:
            self.element_time_17 = 1  # 1 = запись есть

        time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[20]')
        if "item " in time_18.get_attribute("class"):
            self.element_time_18 = 0  # 0 = нет записи
        if "item detection" in time_18.get_attribute("class"):
            self.element_time_18 = 2  # 2 = запись по детекции
        else:
            self.element_time_18 = 1  # 1 = запись есть

        time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[21]')
        if "item " in time_19.get_attribute("class"):
            self.element_time_19 = 0  # 0 = нет записи
        if "item detection" in time_19.get_attribute("class"):
            self.element_time_19 = 2  # 2 = запись по детекции
        else:
            self.element_time_19 = 1  # 1 = запись есть

        time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[22]')
        if "item " in time_20.get_attribute("class"):
            self.element_time_20 = 0  # 0 = нет записи
        if "item detection" in time_20.get_attribute("class"):
            self.element_time_20 = 2  # 2 = запись по детекции
        else:
            self.element_time_20 = 1  # 1 = запись есть

        time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[23]')
        if "item " in time_21.get_attribute("class"):
            self.element_time_21 = 0  # 0 = нет записи
        if "item detection" in time_21.get_attribute("class"):
            self.element_time_21 = 2  # 2 = запись по детекции
        else:
            self.element_time_21 = 1  # 1 = запись есть

        time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[24]')
        if "item " in time_22.get_attribute("class"):
            self.element_time_22 = 0  # 0 = нет записи
        if "item detection" in time_22.get_attribute("class"):
            self.element_time_22 = 2  # 2 = запись по детекции
        else:
            self.element_time_22 = 1  # 1 = запись есть

        time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[25]')
        if "item " in time_23.get_attribute("class"):
            self.element_time_23 = 0  # 0 = нет записи
        if "item detection" in time_23.get_attribute("class"):
            self.element_time_23 = 2  # 2 = запись по детекции
        else:
            self.element_time_23 = 1  # 1 = запись есть

    def saturday(self):
        driver = self.app.driver
        # Суббота
        time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[2]')
        if "item " in time_0.get_attribute("class"):
            self.element_time_0 = 0  # 0 = нет записи
        if "item detection" in time_0.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_0 = 1  # 1 = запись есть

        time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[3]')
        if "item " in time_1.get_attribute("class"):
            self.element_time_1 = 0  # 0 = нет записи
        if "item detection" in time_1.get_attribute("class"):
            self.element_time_1 = 2  # 2 = запись по детекции
        else:
            self.element_time_1 = 1  # 1 = запись есть

        time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[4]')
        if "item " in time_2.get_attribute("class"):
            self.element_time_2 = 0  # 0 = нет записи
        if "item detection" in time_2.get_attribute("class"):
            self.element_time_2 = 2  # 2 = запись по детекции
        else:
            self.element_time_2 = 1  # 1 = запись есть

        time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[5]')
        if "item " in time_3.get_attribute("class"):
            self.element_time_3 = 0  # 0 = нет записи
        if "item detection" in time_3.get_attribute("class"):
            self.element_time_3 = 2  # 2 = запись по детекции
        else:
            self.element_time_3 = 1  # 1 = запись есть

        time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[6]')
        if "item " in time_4.get_attribute("class"):
            self.element_time_4 = 0  # 0 = нет записи
        if "item detection" in time_4.get_attribute("class"):
            self.element_time_4 = 2  # 2 = запись по детекции
        else:
            self.element_time_4 = 1  # 1 = запись есть

        time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[7]')
        if "item " in time_5.get_attribute("class"):
            self.element_time_5 = 0  # 0 = нет записи
        if "item detection" in time_5.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_5 = 1  # 1 = запись есть

        time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[8]')
        if "item " in time_6.get_attribute("class"):
            self.element_time_6 = 0  # 0 = нет записи
        if "item detection" in time_6.get_attribute("class"):
            self.element_time_6 = 2  # 2 = запись по детекции
        else:
            self.element_time_6 = 1  # 1 = запись есть

        time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[9]')
        if "item " in time_7.get_attribute("class"):
            self.element_time_7 = 0  # 0 = нет записи
        if "item detection" in time_7.get_attribute("class"):
            self.element_time_7 = 2  # 2 = запись по детекции
        else:
            self.element_time_7 = 1  # 1 = запись есть

        time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[10]')
        if "item " in time_8.get_attribute("class"):
            self.element_time_8 = 0  # 0 = нет записи
        if "item detection" in time_8.get_attribute("class"):
            self.element_time_8 = 2  # 2 = запись по детекции
        else:
            self.element_time_8 = 1  # 1 = запись есть

        time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[11]')
        if "item " in time_9.get_attribute("class"):
            self.element_time_9 = 0  # 0 = нет записи
        if "item detection" in time_9.get_attribute("class"):
            self.element_time_9 = 2  # 2 = запись по детекции
        else:
            self.element_time_9 = 1  # 1 = запись есть

        time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[12]')
        if "item " in time_10.get_attribute("class"):
            self.element_time_10 = 0  # 0 = нет записи
        if "item detection" in time_10.get_attribute("class"):
            self.element_time_10 = 2  # 2 = запись по детекции
        else:
            self.element_time_10 = 1  # 1 = запись есть

        time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[13]')
        if "item " in time_11.get_attribute("class"):
            self.element_time_11 = 0  # 0 = нет записи
        if "item detection" in time_11.get_attribute("class"):
            self.element_time_11 = 2  # 2 = запись по детекции
        else:
            self.element_time_11 = 1  # 1 = запись есть

        time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[14]')
        if "item " in time_12.get_attribute("class"):
            self.element_time_12 = 0  # 0 = нет записи
        if "item detection" in time_12.get_attribute("class"):
            self.element_time_12 = 2  # 2 = запись по детекции
        else:
            self.element_time_12 = 1  # 1 = запись есть

        time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[15]')
        if "item " in time_13.get_attribute("class"):
            self.element_time_13 = 0  # 0 = нет записи
        if "item detection" in time_13.get_attribute("class"):
            self.element_time_13 = 2  # 2 = запись по детекции
        else:
            self.element_time_13 = 1  # 1 = запись есть

        time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[16]')
        if "item " in time_14.get_attribute("class"):
            self.element_time_14 = 0  # 0 = нет записи
        if "item detection" in time_14.get_attribute("class"):
            self.element_time_14 = 2  # 2 = запись по детекции
        else:
            self.element_time_14 = 1  # 1 = запись есть

        time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[17]')
        if "item " in time_15.get_attribute("class"):
            self.element_time_15 = 0  # 0 = нет записи
        if "item detection" in time_15.get_attribute("class"):
            self.element_time_15 = 2  # 2 = запись по детекции
        else:
            self.element_time_15 = 1  # 1 = запись есть

        time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[18]')
        if "item " in time_16.get_attribute("class"):
            self.element_time_16 = 0  # 0 = нет записи
        if "item detection" in time_16.get_attribute("class"):
            self.element_time_16 = 2  # 2 = запись по детекции
        else:
            self.element_time_16 = 1  # 1 = запись есть

        time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[19]')
        if "item " in time_17.get_attribute("class"):
            self.element_time_17 = 0  # 0 = нет записи
        if "item detection" in time_17.get_attribute("class"):
            self.element_time_17 = 2  # 2 = запись по детекции
        else:
            self.element_time_17 = 1  # 1 = запись есть

        time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[20]')
        if "item " in time_18.get_attribute("class"):
            self.element_time_18 = 0  # 0 = нет записи
        if "item detection" in time_18.get_attribute("class"):
            self.element_time_18 = 2  # 2 = запись по детекции
        else:
            self.element_time_18 = 1  # 1 = запись есть

        time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[21]')
        if "item " in time_19.get_attribute("class"):
            self.element_time_19 = 0  # 0 = нет записи
        if "item detection" in time_19.get_attribute("class"):
            self.element_time_19 = 2  # 2 = запись по детекции
        else:
            self.element_time_19 = 1  # 1 = запись есть

        time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[22]')
        if "item " in time_20.get_attribute("class"):
            self.element_time_20 = 0  # 0 = нет записи
        if "item detection" in time_20.get_attribute("class"):
            self.element_time_20 = 2  # 2 = запись по детекции
        else:
            self.element_time_20 = 1  # 1 = запись есть

        time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[23]')
        if "item " in time_21.get_attribute("class"):
            self.element_time_21 = 0  # 0 = нет записи
        if "item detection" in time_21.get_attribute("class"):
            self.element_time_21 = 2  # 2 = запись по детекции
        else:
            self.element_time_21 = 1  # 1 = запись есть

        time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[24]')
        if "item " in time_22.get_attribute("class"):
            self.element_time_22 = 0  # 0 = нет записи
        if "item detection" in time_22.get_attribute("class"):
            self.element_time_22 = 2  # 2 = запись по детекции
        else:
            self.element_time_22 = 1  # 1 = запись есть

        time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[25]')
        if "item " in time_23.get_attribute("class"):
            self.element_time_23 = 0  # 0 = нет записи
        if "item detection" in time_23.get_attribute("class"):
            self.element_time_23 = 2  # 2 = запись по детекции
        else:
            self.element_time_23 = 1  # 1 = запись есть

    def friday(self):
        driver = self.app.driver
        # Пятница
        time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[2]')
        if "item " in time_0.get_attribute("class"):
            self.element_time_0 = 0  # 0 = нет записи
        if "item detection" in time_0.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_0 = 1  # 1 = запись есть

        time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[3]')
        if "item " in time_1.get_attribute("class"):
            self.element_time_1 = 0  # 0 = нет записи
        if "item detection" in time_1.get_attribute("class"):
            self.element_time_1 = 2  # 2 = запись по детекции
        else:
            self.element_time_1 = 1  # 1 = запись есть

        time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[4]')
        if "item " in time_2.get_attribute("class"):
            self.element_time_2 = 0  # 0 = нет записи
        if "item detection" in time_2.get_attribute("class"):
            self.element_time_2 = 2  # 2 = запись по детекции
        else:
            self.element_time_2 = 1  # 1 = запись есть

        time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[5]')
        if "item " in time_3.get_attribute("class"):
            self.element_time_3 = 0  # 0 = нет записи
        if "item detection" in time_3.get_attribute("class"):
            self.element_time_3 = 2  # 2 = запись по детекции
        else:
            self.element_time_3 = 1  # 1 = запись есть

        time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[6]')
        if "item " in time_4.get_attribute("class"):
            self.element_time_4 = 0  # 0 = нет записи
        if "item detection" in time_4.get_attribute("class"):
            self.element_time_4 = 2  # 2 = запись по детекции
        else:
            self.element_time_4 = 1  # 1 = запись есть

        time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[7]')
        if "item " in time_5.get_attribute("class"):
            self.element_time_5 = 0  # 0 = нет записи
        if "item detection" in time_5.get_attribute("class"):
            self.element_time_5 = 2  # 2 = запись по детекции
        else:
            self.element_time_5 = 1  # 1 = запись есть

        time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[8]')
        if "item " in time_6.get_attribute("class"):
            self.element_time_6 = 0  # 0 = нет записи
        if "item detection" in time_6.get_attribute("class"):
            self.element_time_6 = 2  # 2 = запись по детекции
        else:
            self.element_time_6 = 1  # 1 = запись есть

        time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[9]')
        if "item " in time_7.get_attribute("class"):
            self.element_time_7 = 0  # 0 = нет записи
        if "item detection" in time_7.get_attribute("class"):
            self.element_time_7 = 2  # 2 = запись по детекции
        else:
            self.element_time_7 = 1  # 1 = запись есть

        time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[10]')
        if "item " in time_8.get_attribute("class"):
            self.element_time_8 = 0  # 0 = нет записи
        if "item detection" in time_8.get_attribute("class"):
            self.element_time_8 = 2  # 2 = запись по детекции
        else:
            self.element_time_8 = 1  # 1 = запись есть

        time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[11]')
        if "item " in time_9.get_attribute("class"):
            self.element_time_9 = 0  # 0 = нет записи
        if "item detection" in time_9.get_attribute("class"):
            self.element_time_9 = 2  # 2 = запись по детекции
        else:
            self.element_time_9 = 1  # 1 = запись есть

        time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[12]')
        if "item " in time_10.get_attribute("class"):
            self.element_time_10 = 0  # 0 = нет записи
        if "item detection" in time_10.get_attribute("class"):
            self.element_time_10 = 2  # 2 = запись по детекции
        else:
            self.element_time_10 = 1  # 1 = запись есть

        time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[13]')
        if "item " in time_11.get_attribute("class"):
            self.element_time_11 = 0  # 0 = нет записи
        if "item detection" in time_11.get_attribute("class"):
            self.element_time_11 = 2  # 2 = запись по детекции
        else:
            self.element_time_11 = 1  # 1 = запись есть

        time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[14]')
        if "item " in time_12.get_attribute("class"):
            self.element_time_12 = 0  # 0 = нет записи
        if "item detection" in time_12.get_attribute("class"):
            self.element_time_12 = 2  # 2 = запись по детекции
        else:
            self.element_time_12 = 1  # 1 = запись есть

        time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[15]')
        if "item " in time_13.get_attribute("class"):
            self.element_time_13 = 0  # 0 = нет записи
        if "item detection" in time_13.get_attribute("class"):
            self.element_time_13 = 2  # 2 = запись по детекции
        else:
            self.element_time_13 = 1  # 1 = запись есть

        time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[16]')
        if "item " in time_14.get_attribute("class"):
            self.element_time_14 = 0  # 0 = нет записи
        if "item detection" in time_14.get_attribute("class"):
            self.element_time_14 = 2  # 2 = запись по детекции
        else:
            self.element_time_14 = 1  # 1 = запись есть

        time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[17]')
        if "item " in time_15.get_attribute("class"):
            self.element_time_15 = 0  # 0 = нет записи
        if "item detection" in time_15.get_attribute("class"):
            self.element_time_15 = 2  # 2 = запись по детекции
        else:
            self.element_time_15 = 1  # 1 = запись есть

        time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[18]')
        if "item " in time_16.get_attribute("class"):
            self.element_time_16 = 0  # 0 = нет записи
        if "item detection" in time_16.get_attribute("class"):
            self.element_time_16 = 2  # 2 = запись по детекции
        else:
            self.element_time_16 = 1  # 1 = запись есть

        time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[19]')
        if "item " in time_17.get_attribute("class"):
            self.element_time_17 = 0  # 0 = нет записи
        if "item detection" in time_17.get_attribute("class"):
            self.element_time_17 = 2  # 2 = запись по детекции
        else:
            self.element_time_17 = 1  # 1 = запись есть

        time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[20]')
        if "item " in time_18.get_attribute("class"):
            self.element_time_18 = 0  # 0 = нет записи
        if "item detection" in time_18.get_attribute("class"):
            self.element_time_18 = 2  # 2 = запись по детекции
        else:
            self.element_time_18 = 1  # 1 = запись есть

        time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[21]')
        if "item " in time_19.get_attribute("class"):
            self.element_time_19 = 0  # 0 = нет записи
        if "item detection" in time_19.get_attribute("class"):
            self.element_time_19 = 2  # 2 = запись по детекции
        else:
            self.element_time_19 = 1  # 1 = запись есть

        time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[22]')
        if "item " in time_20.get_attribute("class"):
            self.element_time_20 = 0  # 0 = нет записи
        if "item detection" in time_20.get_attribute("class"):
            self.element_time_20 = 2  # 2 = запись по детекции
        else:
            self.element_time_20 = 1  # 1 = запись есть

        time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[23]')
        if "item " in time_21.get_attribute("class"):
            self.element_time_21 = 0  # 0 = нет записи
        if "item detection" in time_21.get_attribute("class"):
            self.element_time_21 = 2  # 2 = запись по детекции
        else:
            self.element_time_21 = 1  # 1 = запись есть

        time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[24]')
        if "item " in time_22.get_attribute("class"):
            self.element_time_22 = 0  # 0 = нет записи
        if "item detection" in time_22.get_attribute("class"):
            self.element_time_22 = 2  # 2 = запись по детекции
        else:
            self.element_time_22 = 1  # 1 = запись есть

        time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[25]')
        if "item " in time_23.get_attribute("class"):
            self.element_time_23 = 0  # 0 = нет записи
        if "item detection" in time_23.get_attribute("class"):
            self.element_time_23 = 2  # 2 = запись по детекции
        else:
            self.element_time_23 = 1  # 1 = запись есть

    def thursday(self):
        driver = self.app.driver
        # Четверг
        time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[2]')
        if "item " in time_0.get_attribute("class"):
            self.element_time_0 = 0  # 0 = нет записи
        if "item detection" in time_0.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_0 = 1  # 1 = запись есть

        time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[3]')
        if "item " in time_1.get_attribute("class"):
            self.element_time_1 = 0  # 0 = нет записи
        if "item detection" in time_1.get_attribute("class"):
            self.element_time_1 = 2  # 2 = запись по детекции
        else:
            self.element_time_1 = 1  # 1 = запись есть

        time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[4]')
        if "item " in time_2.get_attribute("class"):
            self.element_time_2 = 0  # 0 = нет записи
        if "item detection" in time_2.get_attribute("class"):
            self.element_time_2 = 2  # 2 = запись по детекции
        else:
            self.element_time_2 = 1  # 1 = запись есть

        time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[5]')
        if "item " in time_3.get_attribute("class"):
            self.element_time_3 = 0  # 0 = нет записи
        if "item detection" in time_3.get_attribute("class"):
            self.element_time_3 = 2  # 2 = запись по детекции
        else:
            self.element_time_3 = 1  # 1 = запись есть

        time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[6]')
        if "item " in time_4.get_attribute("class"):
            self.element_time_4 = 0  # 0 = нет записи
        if "item detection" in time_4.get_attribute("class"):
            self.element_time_4 = 2  # 2 = запись по детекции
        else:
            self.element_time_4 = 1  # 1 = запись есть

        time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[7]')
        if "item " in time_5.get_attribute("class"):
            self.element_time_5 = 0  # 0 = нет записи
        if "item detection" in time_5.get_attribute("class"):
            self.element_time_5 = 2  # 2 = запись по детекции
        else:
            self.element_time_5 = 1  # 1 = запись есть

        time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[8]')
        if "item " in time_6.get_attribute("class"):
            self.element_time_6 = 0  # 0 = нет записи
        if "item detection" in time_6.get_attribute("class"):
            self.element_time_6 = 2  # 2 = запись по детекции
        else:
            self.element_time_6 = 1  # 1 = запись есть

        time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[9]')
        if "item " in time_7.get_attribute("class"):
            self.element_time_7 = 0  # 0 = нет записи
        if "item detection" in time_7.get_attribute("class"):
            self.element_time_7 = 2  # 2 = запись по детекции
        else:
            self.element_time_7 = 1  # 1 = запись есть

        time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[10]')
        if "item " in time_8.get_attribute("class"):
            self.element_time_8 = 0  # 0 = нет записи
        if "item detection" in time_8.get_attribute("class"):
            self.element_time_8 = 2  # 2 = запись по детекции
        else:
            self.element_time_8 = 1  # 1 = запись есть

        time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[11]')
        if "item " in time_9.get_attribute("class"):
            self.element_time_9 = 0  # 0 = нет записи
        if "item detection" in time_9.get_attribute("class"):
            self.element_time_9 = 2  # 2 = запись по детекции
        else:
            self.element_time_9 = 1  # 1 = запись есть

        time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[12]')
        if "item " in time_10.get_attribute("class"):
            self.element_time_10 = 0  # 0 = нет записи
        if "item detection" in time_10.get_attribute("class"):
            self.element_time_10 = 2  # 2 = запись по детекции
        else:
            self.element_time_10 = 1  # 1 = запись есть

        time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[13]')
        if "item " in time_11.get_attribute("class"):
            self.element_time_11 = 0  # 0 = нет записи
        if "item detection" in time_11.get_attribute("class"):
            self.element_time_11 = 2  # 2 = запись по детекции
        else:
            self.element_time_11 = 1  # 1 = запись есть

        time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[14]')
        if "item " in time_12.get_attribute("class"):
            self.element_time_12 = 0  # 0 = нет записи
        if "item detection" in time_12.get_attribute("class"):
            self.element_time_12 = 2  # 2 = запись по детекции
        else:
            self.element_time_12 = 1  # 1 = запись есть

        time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[15]')
        if "item " in time_13.get_attribute("class"):
            self.element_time_13 = 0  # 0 = нет записи
        if "item detection" in time_13.get_attribute("class"):
            self.element_time_13 = 2  # 2 = запись по детекции
        else:
            self.element_time_13 = 1  # 1 = запись есть

        time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[16]')
        if "item " in time_14.get_attribute("class"):
            self.element_time_14 = 0  # 0 = нет записи
        if "item detection" in time_14.get_attribute("class"):
            self.element_time_14 = 2  # 2 = запись по детекции
        else:
            self.element_time_14 = 1  # 1 = запись есть

        time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[17]')
        if "item " in time_15.get_attribute("class"):
            self.element_time_15 = 0  # 0 = нет записи
        if "item detection" in time_15.get_attribute("class"):
            self.element_time_15 = 2  # 2 = запись по детекции
        else:
            self.element_time_15 = 1  # 1 = запись есть

        time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[18]')
        if "item " in time_16.get_attribute("class"):
            self.element_time_16 = 0  # 0 = нет записи
        if "item detection" in time_16.get_attribute("class"):
            self.element_time_16 = 2  # 2 = запись по детекции
        else:
            self.element_time_16 = 1  # 1 = запись есть

        time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[19]')
        if "item " in time_17.get_attribute("class"):
            self.element_time_17 = 0  # 0 = нет записи
        if "item detection" in time_17.get_attribute("class"):
            self.element_time_17 = 2  # 2 = запись по детекции
        else:
            self.element_time_17 = 1  # 1 = запись есть

        time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[20]')
        if "item " in time_18.get_attribute("class"):
            self.element_time_18 = 0  # 0 = нет записи
        if "item detection" in time_18.get_attribute("class"):
            self.element_time_18 = 2  # 2 = запись по детекции
        else:
            self.element_time_18 = 1  # 1 = запись есть

        time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[21]')
        if "item " in time_19.get_attribute("class"):
            self.element_time_19 = 0  # 0 = нет записи
        if "item detection" in time_19.get_attribute("class"):
            self.element_time_19 = 2  # 2 = запись по детекции
        else:
            self.element_time_19 = 1  # 1 = запись есть

        time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[22]')
        if "item " in time_20.get_attribute("class"):
            self.element_time_20 = 0  # 0 = нет записи
        if "item detection" in time_20.get_attribute("class"):
            self.element_time_20 = 2  # 2 = запись по детекции
        else:
            self.element_time_20 = 1  # 1 = запись есть

        time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[23]')
        if "item " in time_21.get_attribute("class"):
            self.element_time_21 = 0  # 0 = нет записи
        if "item detection" in time_21.get_attribute("class"):
            self.element_time_21 = 2  # 2 = запись по детекции
        else:
            self.element_time_21 = 1  # 1 = запись есть

        time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[24]')
        if "item " in time_22.get_attribute("class"):
            self.element_time_22 = 0  # 0 = нет записи
        if "item detection" in time_22.get_attribute("class"):
            self.element_time_22 = 2  # 2 = запись по детекции
        else:
            self.element_time_22 = 1  # 1 = запись есть

        time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[25]')
        if "item " in time_23.get_attribute("class"):
            self.element_time_23 = 0  # 0 = нет записи
        if "item detection" in time_23.get_attribute("class"):
            self.element_time_23 = 2  # 2 = запись по детекции
        else:
            self.element_time_23 = 1  # 1 = запись есть

    def wednesday(self):
        driver = self.app.driver
        # Среда
        time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[2]')
        if "item " in time_0.get_attribute("class"):
            self.element_time_0 = 0  # 0 = нет записи
        if "item detection" in time_0.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_0 = 1  # 1 = запись есть

        time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[3]')
        if "item " in time_1.get_attribute("class"):
            self.element_time_1 = 0  # 0 = нет записи
        if "item detection" in time_1.get_attribute("class"):
            self.element_time_1 = 2  # 2 = запись по детекции
        else:
            self.element_time_1 = 1  # 1 = запись есть

        time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[4]')
        if "item " in time_2.get_attribute("class"):
            self.element_time_2 = 0  # 0 = нет записи
        if "item detection" in time_2.get_attribute("class"):
            self.element_time_2 = 2  # 2 = запись по детекции
        else:
            self.element_time_2 = 1  # 1 = запись есть

        time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[5]')
        if "item " in time_3.get_attribute("class"):
            self.element_time_3 = 0  # 0 = нет записи
        if "item detection" in time_3.get_attribute("class"):
            self.element_time_3 = 2  # 2 = запись по детекции
        else:
            self.element_time_3 = 1  # 1 = запись есть

        time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[6]')
        if "item " in time_4.get_attribute("class"):
            self.element_time_4 = 0  # 0 = нет записи
        if "item detection" in time_4.get_attribute("class"):
            self.element_time_4 = 2  # 2 = запись по детекции
        else:
            self.element_time_4 = 1  # 1 = запись есть

        time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[7]')
        if "item " in time_5.get_attribute("class"):
            self.element_time_5 = 0  # 0 = нет записи
        if "item detection" in time_5.get_attribute("class"):
            self.element_time_5 = 2  # 2 = запись по детекции
        else:
            self.element_time_5 = 1  # 1 = запись есть

        time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[8]')
        if "item " in time_6.get_attribute("class"):
            self.element_time_6 = 0  # 0 = нет записи
        if "item detection" in time_6.get_attribute("class"):
            self.element_time_6 = 2  # 2 = запись по детекции
        else:
            self.element_time_6 = 1  # 1 = запись есть

        time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[9]')
        if "item " in time_7.get_attribute("class"):
            self.element_time_7 = 0  # 0 = нет записи
        if "item detection" in time_7.get_attribute("class"):
            self.element_time_7 = 2  # 2 = запись по детекции
        else:
            self.element_time_7 = 1  # 1 = запись есть

        time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[10]')
        if "item " in time_8.get_attribute("class"):
            self.element_time_8 = 0  # 0 = нет записи
        if "item detection" in time_8.get_attribute("class"):
            self.element_time_8 = 2  # 2 = запись по детекции
        else:
            self.element_time_8 = 1  # 1 = запись есть

        time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[11]')
        if "item " in time_9.get_attribute("class"):
            self.element_time_9 = 0  # 0 = нет записи
        if "item detection" in time_9.get_attribute("class"):
            self.element_time_9 = 2  # 2 = запись по детекции
        else:
            self.element_time_9 = 1  # 1 = запись есть

        time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[12]')
        if "item " in time_10.get_attribute("class"):
            self.element_time_10 = 0  # 0 = нет записи
        if "item detection" in time_10.get_attribute("class"):
            self.element_time_10 = 2  # 2 = запись по детекции
        else:
            self.element_time_10 = 1  # 1 = запись есть

        time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[13]')
        if "item " in time_11.get_attribute("class"):
            self.element_time_11 = 0  # 0 = нет записи
        if "item detection" in time_11.get_attribute("class"):
            self.element_time_11 = 2  # 2 = запись по детекции
        else:
            self.element_time_11 = 1  # 1 = запись есть

        time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[14]')
        if "item " in time_12.get_attribute("class"):
            self.element_time_12 = 0  # 0 = нет записи
        if "item detection" in time_12.get_attribute("class"):
            self.element_time_12 = 2  # 2 = запись по детекции
        else:
            self.element_time_12 = 1  # 1 = запись есть

        time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[15]')
        if "item " in time_13.get_attribute("class"):
            self.element_time_13 = 0  # 0 = нет записи
        if "item detection" in time_13.get_attribute("class"):
            self.element_time_13 = 2  # 2 = запись по детекции
        else:
            self.element_time_13 = 1  # 1 = запись есть

        time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[16]')
        if "item " in time_14.get_attribute("class"):
            self.element_time_14 = 0  # 0 = нет записи
        if "item detection" in time_14.get_attribute("class"):
            self.element_time_14 = 2  # 2 = запись по детекции
        else:
            self.element_time_14 = 1  # 1 = запись есть

        time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[17]')
        if "item " in time_15.get_attribute("class"):
            self.element_time_15 = 0  # 0 = нет записи
        if "item detection" in time_15.get_attribute("class"):
            self.element_time_15 = 2  # 2 = запись по детекции
        else:
            self.element_time_15 = 1  # 1 = запись есть

        time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[18]')
        if "item " in time_16.get_attribute("class"):
            self.element_time_16 = 0  # 0 = нет записи
        if "item detection" in time_16.get_attribute("class"):
            self.element_time_16 = 2  # 2 = запись по детекции
        else:
            self.element_time_16 = 1  # 1 = запись есть

        time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[19]')
        if "item " in time_17.get_attribute("class"):
            self.element_time_17 = 0  # 0 = нет записи
        if "item detection" in time_17.get_attribute("class"):
            self.element_time_17 = 2  # 2 = запись по детекции
        else:
            self.element_time_17 = 1  # 1 = запись есть

        time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[20]')
        if "item " in time_18.get_attribute("class"):
            self.element_time_18 = 0  # 0 = нет записи
        if "item detection" in time_18.get_attribute("class"):
            self.element_time_18 = 2  # 2 = запись по детекции
        else:
            self.element_time_18 = 1  # 1 = запись есть

        time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[21]')
        if "item " in time_19.get_attribute("class"):
            self.element_time_19 = 0  # 0 = нет записи
        if "item detection" in time_19.get_attribute("class"):
            self.element_time_19 = 2  # 2 = запись по детекции
        else:
            self.element_time_19 = 1  # 1 = запись есть

        time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[22]')
        if "item " in time_20.get_attribute("class"):
            self.element_time_20 = 0  # 0 = нет записи
        if "item detection" in time_20.get_attribute("class"):
            self.element_time_20 = 2  # 2 = запись по детекции
        else:
            self.element_time_20 = 1  # 1 = запись есть

        time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[23]')
        if "item " in time_21.get_attribute("class"):
            self.element_time_21 = 0  # 0 = нет записи
        if "item detection" in time_21.get_attribute("class"):
            self.element_time_21 = 2  # 2 = запись по детекции
        else:
            self.element_time_21 = 1  # 1 = запись есть

        time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[24]')
        if "item " in time_22.get_attribute("class"):
            self.element_time_22 = 0  # 0 = нет записи
        if "item detection" in time_22.get_attribute("class"):
            self.element_time_22 = 2  # 2 = запись по детекции
        else:
            self.element_time_22 = 1  # 1 = запись есть

        time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[25]')
        if "item " in time_23.get_attribute("class"):
            self.element_time_23 = 0  # 0 = нет записи
        if "item detection" in time_23.get_attribute("class"):
            self.element_time_23 = 2  # 2 = запись по детекции
        else:
            self.element_time_23 = 1  # 1 = запись есть

    def tuesday(self):
        driver = self.app.driver
        # Вторник
        time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[2]')
        if "item " in time_0.get_attribute("class"):
            self.element_time_0 = 0  # 0 = нет записи
        if "item detection" in time_0.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_0 = 1  # 1 = запись есть

        time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[3]')
        if "item " in time_1.get_attribute("class"):
            self.element_time_1 = 0  # 0 = нет записи
        if "item detection" in time_1.get_attribute("class"):
            self.element_time_1 = 2  # 2 = запись по детекции
        else:
            self.element_time_1 = 1  # 1 = запись есть

        time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[4]')
        if "item " in time_2.get_attribute("class"):
            self.element_time_2 = 0  # 0 = нет записи
        if "item detection" in time_2.get_attribute("class"):
            self.element_time_2 = 2  # 2 = запись по детекции
        else:
            self.element_time_2 = 1  # 1 = запись есть

        time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[5]')
        if "item " in time_3.get_attribute("class"):
            self.element_time_3 = 0  # 0 = нет записи
        if "item detection" in time_3.get_attribute("class"):
            self.element_time_3 = 2  # 2 = запись по детекции
        else:
            self.element_time_3 = 1  # 1 = запись есть

        time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[6]')
        if "item " in time_4.get_attribute("class"):
            self.element_time_4 = 0  # 0 = нет записи
        if "item detection" in time_4.get_attribute("class"):
            self.element_time_4 = 2  # 2 = запись по детекции
        else:
            self.element_time_4 = 1  # 1 = запись есть

        time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[7]')
        if "item " in time_5.get_attribute("class"):
            self.element_time_5 = 0  # 0 = нет записи
        if "item detection" in time_5.get_attribute("class"):
            self.element_time_5 = 2  # 2 = запись по детекции
        else:
            self.element_time_5 = 1  # 1 = запись есть

        time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[8]')
        if "item " in time_6.get_attribute("class"):
            self.element_time_6 = 0  # 0 = нет записи
        if "item detection" in time_6.get_attribute("class"):
            self.element_time_6 = 2  # 2 = запись по детекции
        else:
            self.element_time_6 = 1  # 1 = запись есть

        time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[9]')
        if "item " in time_7.get_attribute("class"):
            self.element_time_7 = 0  # 0 = нет записи
        if "item detection" in time_7.get_attribute("class"):
            self.element_time_7 = 2  # 2 = запись по детекции
        else:
            self.element_time_7 = 1  # 1 = запись есть

        time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[10]')
        if "item " in time_8.get_attribute("class"):
            self.element_time_8 = 0  # 0 = нет записи
        if "item detection" in time_8.get_attribute("class"):
            self.element_time_8 = 2  # 2 = запись по детекции
        else:
            self.element_time_8 = 1  # 1 = запись есть

        time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[11]')
        if "item " in time_9.get_attribute("class"):
            self.element_time_9 = 0  # 0 = нет записи
        if "item detection" in time_9.get_attribute("class"):
            self.element_time_9 = 2  # 2 = запись по детекции
        else:
            self.element_time_9 = 1  # 1 = запись есть

        time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[12]')
        if "item " in time_10.get_attribute("class"):
            self.element_time_10 = 0  # 0 = нет записи
        if "item detection" in time_10.get_attribute("class"):
            self.element_time_10 = 2  # 2 = запись по детекции
        else:
            self.element_time_10 = 1  # 1 = запись есть

        time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[13]')
        if "item " in time_11.get_attribute("class"):
            self.element_time_11 = 0  # 0 = нет записи
        if "item detection" in time_11.get_attribute("class"):
            self.element_time_11 = 2  # 2 = запись по детекции
        else:
            self.element_time_11 = 1  # 1 = запись есть

        time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[14]')
        if "item " in time_12.get_attribute("class"):
            self.element_time_12 = 0  # 0 = нет записи
            if "item detection" in time_12.get_attribute("class"):
                self.element_time_12 = 2  # 2 = запись по детекции
        else:
            self.element_time_12 = 1  # 1 = запись есть

        time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[15]')
        if "item " in time_13.get_attribute("class"):
            self.element_time_13 = 0  # 0 = нет записи
        if "item detection" in time_13.get_attribute("class"):
            self.element_time_13 = 2  # 2 = запись по детекции
        else:
            self.element_time_13 = 1  # 1 = запись есть

        time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[16]')
        if "item " in time_14.get_attribute("class"):
            self.element_time_14 = 0  # 0 = нет записи
        if "item detection" in time_14.get_attribute("class"):
            self.element_time_14 = 2  # 2 = запись по детекции
        else:
            self.element_time_14 = 1  # 1 = запись есть

        time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[17]')
        if "item " in time_15.get_attribute("class"):
            self.element_time_15 = 0  # 0 = нет записи
        if "item detection" in time_15.get_attribute("class"):
            self.element_time_15 = 2  # 2 = запись по детекции
        else:
            self.element_time_15 = 1  # 1 = запись есть

        time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[18]')
        if "item " in time_16.get_attribute("class"):
            self.element_time_16 = 0  # 0 = нет записи
        if "item detection" in time_16.get_attribute("class"):
            self.element_time_16 = 2  # 2 = запись по детекции
        else:
            self.element_time_16 = 1  # 1 = запись есть

        time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[19]')
        if "item " in time_17.get_attribute("class"):
            self.element_time_17 = 0  # 0 = нет записи
        if "item detection" in time_17.get_attribute("class"):
            self.element_time_17 = 2  # 2 = запись по детекции
        else:
            self.element_time_17 = 1  # 1 = запись есть

        time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[20]')
        if "item " in time_18.get_attribute("class"):
            self.element_time_18 = 0  # 0 = нет записи
        if "item detection" in time_18.get_attribute("class"):
            self.element_time_18 = 2  # 2 = запись по детекции
        else:
            self.element_time_18 = 1  # 1 = запись есть

        time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[21]')
        if "item " in time_19.get_attribute("class"):
            self.element_time_19 = 0  # 0 = нет записи
        if "item detection" in time_19.get_attribute("class"):
            self.element_time_19 = 2  # 2 = запись по детекции
        else:
            self.element_time_19 = 1  # 1 = запись есть

        time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[22]')
        if "item " in time_20.get_attribute("class"):
            self.element_time_20 = 0  # 0 = нет записи
        if "item detection" in time_20.get_attribute("class"):
            self.element_time_20 = 2  # 2 = запись по детекции
        else:
            self.element_time_20 = 1  # 1 = запись есть

        time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[23]')
        if "item " in time_21.get_attribute("class"):
            self.element_time_21 = 0  # 0 = нет записи
            if "item detection" in time_21.get_attribute("class"):
                self.element_time_21 = 2  # 2 = запись по детекции
        else:
            self.element_time_21 = 1  # 1 = запись есть

        time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[24]')
        if "item " in time_22.get_attribute("class"):
            self.element_time_22 = 0  # 0 = нет записи
        if "item detection" in time_22.get_attribute("class"):
            self.element_time_22 = 2  # 2 = запись по детекции
        else:
            self.element_time_22 = 1  # 1 = запись есть

        time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[25]')
        if "item " in time_23.get_attribute("class"):
            self.element_time_23 = 0  # 0 = нет записи
        if "item detection" in time_23.get_attribute("class"):
            self.element_time_23 = 2  # 2 = запись по детекции
        else:
            self.element_time_23 = 1  # 1 = запись есть

    def monday(self):
        driver = self.app.driver
        # Понедельник
        time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[2]')
        if "item " in time_0.get_attribute("class"):
            self.element_time_0 = 0  # 0 = нет записи
        if "item detection" in time_0.get_attribute("class"):
            self.element_time_0 = 2  # 2 = запись по детекции
        else:
            self.element_time_0 = 1  # 1 = запись есть

        time_1 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[3]')
        if "item " in time_1.get_attribute("class"):
            self.element_time_1 = 0  # 0 = нет записи
        if "item detection" in time_1.get_attribute("class"):
            self.element_time_1 = 2  # 2 = запись по детекции
        else:
            self.element_time_1 = 1  # 1 = запись есть

        time_2 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[4]')
        if "item " in time_2.get_attribute("class"):
            self.element_time_2 = 0  # 0 = нет записи
        if "item detection" in time_2.get_attribute("class"):
            self.element_time_2 = 2  # 2 = запись по детекции
        else:
            self.element_time_2 = 1  # 1 = запись есть

        time_3 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[5]')
        if "item " in time_3.get_attribute("class"):
            self.element_time_3 = 0  # 0 = нет записи
        if "item detection" in time_3.get_attribute("class"):
            self.element_time_3 = 2  # 2 = запись по детекции
        else:
            self.element_time_3 = 1  # 1 = запись есть

        time_4 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[6]')
        if "item " in time_4.get_attribute("class"):
            self.element_time_4 = 0  # 0 = нет записи
        if "item detection" in time_4.get_attribute("class"):
            self.element_time_4 = 2  # 2 = запись по детекции
        else:
            self.element_time_4 = 1  # 1 = запись есть

        time_5 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[7]')
        if "item " in time_5.get_attribute("class"):
            self.element_time_5 = 0  # 0 = нет записи
        if "item detection" in time_5.get_attribute("class"):
            self.element_time_5 = 2  # 2 = запись по детекции
        else:
            self.element_time_5 = 1  # 1 = запись есть

        time_6 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[8]')
        if "item " in time_6.get_attribute("class"):
            self.element_time_6 = 0  # 0 = нет записи
        if "item detection" in time_6.get_attribute("class"):
            self.element_time_6 = 2  # 2 = запись по детекции
        else:
            self.element_time_6 = 1  # 1 = запись есть

        time_7 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[9]')
        if "item " in time_7.get_attribute("class"):
            self.element_time_7 = 0  # 0 = нет записи
        if "item detection" in time_7.get_attribute("class"):
            self.element_time_7 = 2  # 2 = запись по детекции
        else:
            self.element_time_7 = 1  # 1 = запись есть

        time_8 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[10]')
        if "item " in time_8.get_attribute("class"):
            self.element_time_8 = 0  # 0 = нет записи
        if "item detection" in time_8.get_attribute("class"):
            self.element_time_8 = 2  # 2 = запись по детекции
        else:
            self.element_time_8 = 1  # 1 = запись есть

        time_9 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[11]')
        if "item " in time_9.get_attribute("class"):
            self.element_time_9 = 0  # 0 = нет записи
        if "item detection" in time_9.get_attribute("class"):
            self.element_time_9 = 2  # 2 = запись по детекции
        else:
            self.element_time_9 = 1  # 1 = запись есть

        time_10 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[12]')
        if "item " in time_10.get_attribute("class"):
            self.element_time_10 = 0  # 0 = нет записи
        if "item detection" in time_10.get_attribute("class"):
            self.element_time_10 = 2  # 2 = запись по детекции
        else:
            self.element_time_10 = 1  # 1 = запись есть

        time_11 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[13]')
        if "item " in time_11.get_attribute("class"):
            self.element_time_11 = 0  # 0 = нет записи
        if "item detection" in time_11.get_attribute("class"):
            self.element_time_11 = 2  # 2 = запись по детекции
        else:
            self.element_time_11 = 1  # 1 = запись есть

        time_12 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[14]')
        if "item " in time_12.get_attribute("class"):
            self.element_time_12 = 0  # 0 = нет записи
        if "item detection" in time_12.get_attribute("class"):
            self.element_time_12 = 2  # 2 = запись по детекции
        else:
            self.element_time_12 = 1  # 1 = запись есть

        time_13 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[15]')
        if "item " in time_13.get_attribute("class"):
            self.element_time_13 = 0  # 0 = нет записи
        if "item detection" in time_13.get_attribute("class"):
            self.element_time_13 = 2  # 2 = запись по детекции
        else:
            self.element_time_13 = 1  # 1 = запись есть

        time_14 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[16]')
        if "item " in time_14.get_attribute("class"):
            self.element_time_14 = 0  # 0 = нет записи
        if "item detection" in time_14.get_attribute("class"):
            self.element_time_14 = 2  # 2 = запись по детекции
        else:
            self.element_time_14 = 1  # 1 = запись есть

        time_15 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[17]')
        if "item " in time_15.get_attribute("class"):
            self.element_time_15 = 0  # 0 = нет записи
        if "item detection" in time_15.get_attribute("class"):
            self.element_time_15 = 2  # 2 = запись по детекции
        else:
            self.element_time_15 = 1  # 1 = запись есть

        time_16 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[18]')
        if "item " in time_16.get_attribute("class"):
            self.element_time_16 = 0  # 0 = нет записи
        if "item detection" in time_16.get_attribute("class"):
            self.element_time_16 = 2  # 2 = запись по детекции
        else:
            self.element_time_16 = 1  # 1 = запись есть

        time_17 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[19]')
        if "item " in time_17.get_attribute("class"):
            self.element_time_17 = 0  # 0 = нет записи
        if "item detection" in time_17.get_attribute("class"):
            self.element_time_17 = 2  # 2 = запись по детекции
        else:
            self.element_time_17 = 1  # 1 = запись есть

        time_18 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[20]')
        if "item " in time_18.get_attribute("class"):
            self.element_time_18 = 0  # 0 = нет записи
        if "item detection" in time_18.get_attribute("class"):
            self.element_time_18 = 2  # 2 = запись по детекции
        else:
            self.element_time_18 = 1  # 1 = запись есть

        time_19 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[21]')
        if "item " in time_19.get_attribute("class"):
            self.element_time_19 = 0  # 0 = нет записи
        if "item detection" in time_19.get_attribute("class"):
            self.element_time_19 = 2  # 2 = запись по детекции
        else:
            self.element_time_19 = 1  # 1 = запись есть

        time_20 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[22]')
        if "item " in time_20.get_attribute("class"):
            self.element_time_20 = 0  # 0 = нет записи
        if "item detection" in time_20.get_attribute("class"):
            self.element_time_20 = 2  # 2 = запись по детекции
        else:
            self.element_time_20 = 1  # 1 = запись есть

        time_21 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[23]')
        if "item " in time_21.get_attribute("class"):
            self.element_time_21 = 0  # 0 = нет записи
        if "item detection" in time_21.get_attribute("class"):
            self.element_time_21 = 2  # 2 = запись по детекции
        else:
            self.element_time_21 = 1  # 1 = запись есть

        time_22 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[24]')
        if "item " in time_22.get_attribute("class"):
            self.element_time_22 = 0  # 0 = нет записи
        if "item detection" in time_22.get_attribute("class"):
            self.element_time_22 = 2  # 2 = запись по детекции
        else:
            self.element_time_22 = 1  # 1 = запись есть

        time_23 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[25]')
        if "item " in time_23.get_attribute("class"):
            self.element_time_23 = 0  # 0 = нет записи
        if "item detection" in time_23.get_attribute("class"):
            self.element_time_23 = 2  # 2 = запись по детекции
        else:
            self.element_time_23 = 1  # 1 = запись есть



