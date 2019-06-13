class hours:

    def __init__(self, app):
        self.app = app


    def check_time_0(self):
        driver = self.app.driver
        for i in range(0, 5, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_0
            self.check_for_emptiness()

    def check_time_1(self):
        driver = self.app.driver
        for i in range(5, 10, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_1
            self.check_for_emptiness()

    def check_time_2(self):
        driver = self.app.driver
        for i in range(10, 15, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_2
            self.check_for_emptiness()

    def check_time_3(self):
        driver = self.app.driver
        for i in range(15, 20, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_3
            self.check_for_emptiness()

    def check_time_4(self):
        driver = self.app.driver
        for i in range(20, 25, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_4
            self.check_for_emptiness()

    def check_time_5(self):
        driver = self.app.driver
        for i in range(25, 30, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_5
            self.check_for_emptiness()

    def check_time_6(self):
        driver = self.app.driver
        for i in range(30, 35, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_6
            self.check_for_emptiness()

    def check_time_7(self):
        driver = self.app.driver
        for i in range(35, 40, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_7
            self.check_for_emptiness()



    def check_time_8(self):
        driver = self.app.driver
        for i in range(40, 45, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_8
            self.check_for_emptiness()

    def check_time_9(self):
        driver = self.app.driver
        for i in range(45, 50, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_9
            self.check_for_emptiness()

    def check_time_10(self):
        driver = self.app.driver
        for i in range(50, 55, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_10
            self.check_for_emptiness()

    def check_time_11(self):
        driver = self.app.driver
        for i in range(55, 60, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_11
            self.check_for_emptiness()

    def check_time_12(self):
        driver = self.app.driver
        for i in range(60, 65, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_12
            self.check_for_emptiness()

    def check_time_13(self):
        driver = self.app.driver
        for i in range(65, 70, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_13
            self.check_for_emptiness()

    def check_time_14(self):
        driver = self.app.driver
        for i in range(70, 75, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_14
            self.check_for_emptiness()

    def check_time_15(self):
        driver = self.app.driver
        for i in range(75, 80, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_15
            self.check_for_emptiness()

    def check_time_16(self):
        driver = self.app.driver
        for i in range(80, 85, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_16
            self.check_for_emptiness()

    def check_time_17(self):
        driver = self.app.driver
        for i in range(85, 90, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_17
            self.check_for_emptiness()

    def check_time_18(self):
        driver = self.app.driver
        for i in range(90, 95, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_18
            self.check_for_emptiness()

    def check_time_19(self):
        driver = self.app.driver
        for i in range(95, 100, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_19
            self.check_for_emptiness()

    def check_time_20(self):
        driver = self.app.driver
        for i in range(100, 105, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_20
            self.check_for_emptiness()

    def check_time_21(self):
        driver = self.app.driver
        for i in range(105, 110, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_21
            self.check_for_emptiness()

    def check_time_22(self):
        driver = self.app.driver
        for i in range(110, 115, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_22
            self.check_for_emptiness()


    def check_time_23(self):
        driver = self.app.driver
        for i in range(115, 120, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            self.ii = i
            self.item_time = self.app.Schedule.element_time_23
            self.check_for_emptiness()

    def check_for_emptiness(self):
        if "item empty " in self.T.get_attribute('class'):
            item = 0
            if item == self.item_time:
                print('роверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
                    self.ii) + ' нет по расписанию.')
                with open('monitoring report.txt', 'a', encoding='utf-8') as f:
                    f.write(
                    '"' + self.app.Monitoring.strg_today + '" INFO: Проверка для камеры "' + self.app.Monitoring.camera_name.strip() + '". Архива ' + str(
                        self.ii) + ' нет по расписанию.\n')
                    f.close()
            else:
                print(
                'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
                    self.ii) + ' нет.')

                with open('monitoring error report.txt', 'a', encoding='utf-8') as f:
                    f.write(
                    '"' + self.app.Monitoring.strg_today + '" WARNING: Проверка для камеры "' + self.app.Monitoring.camera_name.strip() + '". Архива ' + str(
                        self.ii) + ' нет.\n')
                    f.close()
        else:
            self.T.click()
            self.app.Monitoring.check_player()