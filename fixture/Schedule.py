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

    def date(self):
        driver = self.app.driver

        now = datetime.datetime.today()
        cur_day = now.weekday()
        yesterday_weekday = cur_day - 1

        td_weekday = driver.find_elements_by_css_selector('td.weekday')


        Monday = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]')
        Monday.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item"]')


    def items_schedule(self):
        driver = self.app.driver
        self.item1 = 1
        self.item2 = 1    # 1 = постоянная запись
        self.item3 = 1
        self.item4 = 1
        self.item5 = 1
        self.item6 = 1
        self.item7 = 1
        self.item8 = 1
        self.item9 = 1
        self.item10 = 1
        self.item11 = 1
        self.item12 = 1
        self.item13 = 1
        self.item14 = 1
        self.item15 = 1
        self.item16 = 1
        self.item17 = 1
        self.item18 = 1
        self.item19 = 1
        self.item20 = 1
        self.item21 = 1
        self.item22 = 1
        self.item23 = 1
        self.item24 = 1


    def item_time(self):
        driver = self.app.driver

        # time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/div[1]/div[1]')
        item_time_0 = driver.find_element(By.XPATH, '//*[@id="schedule"]/table[1]/tbody/tr[1]/td[2]')
        if driver.find_element(By.CSS_SELECTOR, 'td.item.constant'):
            self.element_time_0 = 1
        elif driver.find_element(By.CSS_SELECTOR, 'td.item.button'):
            self.element_time_0 = 2
        elif driver.find_element(By.CSS_SELECTOR, 'td.item.detection'):
            self.element_time_0 = 3
        elif driver.find_element(By.CSS_SELECTOR, 'td.item.empty'):
            self.element_time_0 = 0
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


