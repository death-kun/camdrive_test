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
        time.sleep(1)
        for i in range(0, 119):
            time_item_button = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant"]')[i]
            time_item_button.click()
            time.sleep(1)
            try:
                driver.find_element_by_css_selector('div.hover-video')

                print('Проверка прошла успешно' + str(i))
            except NoSuchElementException:
                print('Проверка провалилась'  + str(i))
      