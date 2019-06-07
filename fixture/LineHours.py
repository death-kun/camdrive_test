class hours:

    def __init__(self, app):
        self.app = app


    def check_time_0(self):
        driver = self.app.driver
        for i in range(0, 5, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_1(self):
        driver = self.app.driver
        for i in range(5, 10, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_2(self):
        driver = self.app.driver
        for i in range(10, 15, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_3(self):
        driver = self.app.driver
        for i in range(15, 20, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_4(self):
        driver = self.app.driver
        for i in range(20, 25, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_5(self):
        driver = self.app.driver
        for i in range(25, 30, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_6(self):
        driver = self.app.driver
        for i in range(30, 35, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_7(self):
        driver = self.app.driver
        for i in range(35, 40, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_8(self):
        driver = self.app.driver
        for i in range(40, 45, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_9(self):
        driver = self.app.driver
        for i in range(45, 50, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_10(self):
        driver = self.app.driver
        for i in range(50, 55, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_11(self):
        driver = self.app.driver
        for i in range(55, 60, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_12(self):
        driver = self.app.driver
        for i in range(60, 65, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_13(self):
        driver = self.app.driver
        for i in range(65, 70, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_14(self):
        driver = self.app.driver
        for i in range(70, 75, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_15(self):
        driver = self.app.driver
        for i in range(75, 80, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_16(self):
        driver = self.app.driver
        for i in range(80, 85, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_17(self):
        driver = self.app.driver
        for i in range(85, 90, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_18(self):
        driver = self.app.driver
        for i in range(90, 95, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_19(self):
        driver = self.app.driver
        line_19 = driver.find_element_by_xpath('//*[@id="20"]')
        for i in range(95, 100, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_20(self):
        driver = self.app.driver
        for i in range(100, 105, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_21(self):
        driver = self.app.driver
        for i in range(105, 110, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_time_22(self):
        driver = self.app.driver
        for i in range(110, 115, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()


    def check_time_23(self):
        driver = self.app.driver
        for i in range(115, 120, 1):
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[
                i]
            self.check_schedule()
            self.T.click()
            self.ii = i
            self.app.Monitoring.check_player()

    def check_schedule(self):

        if self.T.find_elements_by_css_selector('item empty'):
            print(
                'Проверка, что открывается каждый контейнер с архивом за Вчерашний день.  Архива ' + str(self.ii) + ' нет.')

            with open('monitoring report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"' + self.app.strg_today + '" Проверка для камеры "' + self.app.camera_name.strip() + '". Архива ' + str(self.ii) + ' нет.\n')
                f.close()
        else:
            self.T.click()

