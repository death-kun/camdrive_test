import time
import datetime
from selenium.common.exceptions import NoSuchElementException



class monitoring:

    def __init__(self, app):
        self.app = app

    def archive_length_determination(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        time.sleep(3)
        now = datetime.datetime.now()
        cur_day = now.day
        yesterday = str(cur_day - 1)
        yesterday_button = driver.find_element_by_xpath('//div[contains(text(), "' + yesterday + '")]')
        time.sleep(1)
        yesterday_button.click()
        time.sleep(2)
        for i in range(0, 120):
            time_item_button = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant"]')[i]
            time_item_button.click()
            time.sleep(5)
            #Проверка, что открывается каждый контейнер с архивом за Вчерашний день
            try:
                driver.find_element_by_css_selector('div.hover-video')
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[2]')
                driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()
                print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(i) + ' загрузилось')
            except NoSuchElementException:
                print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Видео '  + str(i) + ' не загрузилось')
