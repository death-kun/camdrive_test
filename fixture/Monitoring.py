import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class monitoring:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        driver = self.app.driver
        self.login_monitoring()
        self.app.Schedule.open_schedule()
        time.sleep(5)
        self.app.Schedule.item_time()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        time.sleep(3)

        # self.check_first_tree()
        #
        # time.sleep(2)
        #
        # self.click_CD630_910D_ms6_dev()
        # time.sleep(2)
        # self.check_camera_CD630_910D_ms6_dev()
        #
        # self.click_CD320_AA06_ms3_dev()
        # time.sleep(2)
        # self.check_camera_CD320_AA06_ms3_dev()
        #
        # self.click_CD320_AA78_ms5()
        # time.sleep(4)
        # self.check_camera_CD320_AA78_ms5()
        #
        # self.click_CD310_2E51_ms4_dev()
        # time.sleep(4)
        # self.check_camera_CD310_2E51_ms4_dev()


        self.check_second_tree()

        time.sleep(2)

        self.click_CD100_E772_ms4()
        time.sleep(2)
        self.check_camera_CD100_E772_ms4()

        self.click_N1001_3A00_bwd()
        time.sleep(2)
        self.check_camera_N1001_3A00_bwd()

        self.click_CD600_EF78_ms6_serv()
        time.sleep(2)
        self.check_camera_CD600_EF78_ms6_serv()

        self.click_CD100_E778_ms5()
        time.sleep(2)
        self.check_camera_CD100_E778_ms5()

        self.click_CD100_E75A_ms3_dev()
        time.sleep(2)
        self.check_camera_CD100_E75A_ms3_dev()

        self.app.logout_butten()

    def click_CD100_E75A_ms3_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12597"]/a').click()  # камера CD100(E75A)_ms3_dev

    def click_CD100_E778_ms5(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_6827"]/a').click()  # камера CD100(E778)_ms5_ПЗ

    def click_CD600_EF78_ms6_serv(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12601"]/a').click()  # камера CD600(EF78)_ms6_serv

    def click_N1001_3A00_bwd(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_14875"]/a').click()  # камера N1001(3A00)_bwd

    def click_CD100_E772_ms4(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_6830"]/a').click()  # камера CD100(E772)_ms4_ПЗ

    def click_CD310_2E51_ms4_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_13959"]/a').click()  # камера CD310(2E51)_ms4_dev

    def click_CD320_AA78_ms5(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_11460"]/a').click()  # камера CD320(AA78)_ms5_Пр_С

    def click_CD320_AA06_ms3_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12603"]/a').click()  # камера CD320(AA06)_ms3_dev

    def click_CD630_910D_ms6_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12602"]/a').click()  # камера CD630(910D)_ms6_dev

    def check_second_tree(self):
        driver = self.app.driver
        try:
            self.app.second_tree()
        except NoSuchElementException:
            driver.find_element_by_xpath('//*[@id="node_12605"]/ins').click()

    def check_first_tree(self):
        driver = self.app.driver
        try:
            self.app.first_tree()
        except NoSuchElementException:
            driver.find_element_by_xpath('//*[@id="node_12604"]/ins').click()

    def check_camera_CD630_910D_ms6_dev(self):
        self.archive_check()

    def check_camera_CD320_AA06_ms3_dev(self):
        self.archive_check()

    def check_camera_CD320_AA78_ms5(self):
        self.archive_check()

    def check_camera_CD310_2E51_ms4_dev(self):
        self.archive_check()

    def check_camera_CD100_E772_ms4(self):
        self.archive_check()

    def check_camera_N1001_3A00_bwd(self):
        self.archive_check()

    def check_camera_CD600_EF78_ms6_serv(self):
        self.archive_check()

    def check_camera_CD100_E778_ms5(self):
        self.archive_check()

    def check_camera_CD100_E75A_ms3_dev(self):
        self.archive_check()


    def archive_check(self):
        driver = self.app.driver
        now = datetime.datetime.now()
        cur_day = now.day
        strg_today = now.strftime('%B %d, %Y')
        yesterday = str(cur_day - 1)
        driver.find_element_by_xpath('//div[contains(text(), "' + yesterday + '")]').click()
        time.sleep(4)

        for y in range(1, 25, 1):
            self.item_element_y = driver.find_element_by_xpath('//*[@id="'+ str(y) +'"]')
            for i in range(0, 120, 1):
                self.time_item_button = driver.find_elements_by_xpath('//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty"]')[i]
                element_item_time_0 = self.element_0()

                assert element_item_time_0 == self.app.Schedule.element_time_0, 'Расписание не совпадает'

                self.time_item_button.click()

            # Проверка, что открывается каждый контейнер с архивом за Вчерашний день
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.hover-video")))


                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.player-main-controlbar-seek-hover")))

                        if driver.find_element_by_css_selector('div.seek-total-time'):
                            archive_duration = driver.find_element_by_css_selector('div.seek-total-time')
                            archive_time = archive_duration.get_attribute('innerHTML')

                            camera_name = self.title()

                            print(
                            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                                i) + ' загрузилось. Длительность видео ' +  archive_time.strip() + ' минут.')

                            with open('monitoring report.txt', 'a', encoding='utf-8') as f:
                                f.write('"' + strg_today + '" Проверка для камеры "' + camera_name.strip() + '" прошла успешно. Видео ' + str(i) + ' загрузилось. Длительность видео ' + archive_time.strip() + ' минут.\n')
                                f.close()

                            driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()
                        else:
                            camera_name = self.title()
                            print(
                            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Видео ' + str(
                                i) + ' не загрузилось')

                            with open('monitoring report.txt', 'a', encoding='utf-8') as f:
                                f.write(
                                '"' + strg_today + '" Проверка для камеры "' + camera_name.strip() + '" провалилась. Видео ' + str(
                                    i) + ' не загрузилось.\n')
                                f.close()

                            driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()

                    except TimeoutException:
                        camera_name = self.title()

                        print(
                        'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Видео ' + str(
                            i) + ' не отображается')

                        with open('monitoring report.txt', 'a', encoding='utf-8') as f:
                            f.write(
                            '"' + strg_today + '" Проверка для камеры "' + camera_name.strip() + '" провалилась. Видео ' + str(
                                i) + ' не отображается.\n')
                            f.close()

                        driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()


                except NoSuchElementException:
                    camera_name = self.title()

                    print(
                    'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Плеер ' + str(i) + ' не отобразился.')

                    with open('monitoring report.txt', 'a', encoding='utf-8') as f:
                        f.write('"' + strg_today + '" Проверка для камеры "' + camera_name.strip() + '" провалилась. Плеер ' + str(i) + ' не отобразился.\n')
                        f.close()

    def element_0(self):
        item_time_0 = self.item_element_y
        if item_time_0.find_element_by_css_selector('div.time.item.constant'):
            self.element_item_time_0 = 1
        elif item_time_0.find_element_by_css_selector('div.time.item.button'):
            self.element_item_time_0 = 2
        elif item_time_0.find_element_by_css_selector('div.time.item.detection'):
            self.element_item_time_0 = 3
        elif item_time_0.find_element_by_css_selector('div.item.empty'):
            self.element_item_time_0 = 4
        return self.element_item_time_0

    def title(self):
        driver = self.app.driver
        camera_title = driver.find_element_by_css_selector('div.title')
        camera_name = camera_title.get_attribute('innerHTML')
        return camera_name

    def opem_LK_monitoring(self):
        driver = self.app.driver
        driver.get('https://www.camdrive.com')

    def login_monitoring(self):
        driver = self.app.driver
        self.opem_LK_monitoring()
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('service')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('7ujm6yhn')
        driver.find_element_by_id('login').click()
        time.sleep(1)

