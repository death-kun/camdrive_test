import time
import datetime
from selenium.common.exceptions import NoSuchElementException

class monitoring:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        driver = self.app.driver
        self.login_monitoring()
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        time.sleep(3)

        try:
            camera_CD630_910D = driver.find_element_by_xpath('//*[@id="node_12602"]/a')
            camera_CD320_AA06 = driver.find_element_by_xpath('//*[@id="node_12603"]/a')
            camera_CD320_AA78 = driver.find_element_by_xpath('//*[@id="node_11460"]/a')
            camera_CD310_2E51 = driver.find_element_by_xpath('//*[@id="node_13959"]/a')
        except NoSuchElementException:
            driver.find_element_by_xpath('//*[@id="node_12604"]/ins').click()

        time.sleep(2)

        camera_CD630_910D.click() #камера CD630(910D)_ms6_dev
        time.sleep(2)
        self.check_camera_CD630_910D_ms6_dev()
        camera_CD320_AA06.click() #камера CD320(AA06)_ms3_dev
        time.sleep(2)
        self.check_camera_CD320_AA06_ms3_dev()
        camera_CD320_AA78.click() #камера CD320(AA78)_ms5_Пр_С
        time.sleep(2)
        self.check_camera_CD320_AA78_ms5()
        camera_CD310_2E51.click() #камера CD310(2E51)_ms4_dev
        time.sleep(2)
        self.check_camera_CD310_2E51_ms4_dev()

        try:
            camera_CD100_E772 = driver.find_element_by_xpath('//*[@id="node_6830"]/a')
            camera_N1001_3A00 = driver.find_element_by_xpath('//*[@id="node_14875"]/a')
            camera_CD600_EF78 = driver.find_element_by_xpath('//*[@id="node_12601"]/a')
            camera_CD100_E778 = driver.find_element_by_xpath('//*[@id="node_6827"]/a')
            camera_CD100_E75A = driver.find_element_by_xpath('//*[@id="node_12597"]/a')
        except NoSuchElementException:
            driver.find_element_by_xpath('//*[@id="node_12605"]/ins').click()

        time.sleep(2)

        camera_CD100_E772.click() #камера CD100(E772)_ms4_ПЗ
        time.sleep(2)
        self.check_camera_CD100_E772_ms4()
        camera_N1001_3A00.click() #камера N1001(3A00)_bwd
        time.sleep(2)
        self.check_camera_N1001_3A00_bwd()
        camera_CD600_EF78.click() #камера CD600(EF78)_ms6_serv
        time.sleep(2)
        self.check_camera_CD600_EF78_ms6_serv()
        camera_CD100_E778.click() #камера CD100(E778)_ms5_ПЗ
        time.sleep(2)
        self.check_camera_CD100_E778_ms5()
        camera_CD100_E75A.click() #камера CD100(E75A)_ms3_dev
        time.sleep(2)
        self.check_camera_CD100_E75A_ms3_dev()

        self.app.logout_butten()


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
        yesterday = str(cur_day - 1)
        yesterday_button = driver.find_element_by_xpath('//div[contains(text(), "' + yesterday + '")]')
        time.sleep(1)
        yesterday_button.click()
        time.sleep(2)
        for i in range(0, 120):
            time_item_button = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant"]')[
                i]
            time_item_button.click()
            time.sleep(5)
            # Проверка, что открывается каждый контейнер с архивом за Вчерашний день
            try:
                driver.find_element_by_css_selector('div.hover-video')
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[2]')

                archive_duration = driver.find_element_by_css_selector('div.seek-total-time')
                archive_time = archive_duration.get_attribute('innerHTML')

                print(
                    'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                        i) + ' загрузилось. Длительность видео ' +  archive_time.strip() + ' минут.')
                f = open('/home/mikhail/PycharmProjects/camdrive_test/monitoring report.txt', 'a' )
                f.write('Проверка прошла успешно. ' + str(
                    i) + ' Видео загрузилось. Длительность видео ' +  archive_time.strip() + ' минут.\n')
                f.close()

                driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()

            except NoSuchElementException:
                print(
                    'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Видео ' + str(
                        i) + ' не загрузилось')
                f = open('/home/mikhail/PycharmProjects/camdrive_test/monitoring report.txt', 'a')
                f.write('Проверка провалилась. ' + str(i) + ' Видео не загрузилось.\n')
                f.close()

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

