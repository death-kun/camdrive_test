import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
import lxml.html as html

class monitoring:

    def __init__(self, app):
        self.app = app

    def detection_of_archive(self):
        self.delete_txt()
        self.app.login_autotest()
        # self.login_monitoring()
        time.sleep(4)

        # Камеры для проверки на тестовом сервере
        self.click_CD120_D521()
        self.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD120_D521()

        time.sleep(2)

        self.click_CD_120()
        self.open_schedule_open_archive()
        time.sleep(4)
        self.check_camera_CD_120()

        # Камеры для проверке на рабочем сервере
        # self.check_first_tree()
        #
        # time.sleep(2)
        #
        # self.click_CD630_910D_ms6_dev()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD630_910D_ms6_dev()
        #
        # self.click_CD320_AA06_ms3_dev()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD320_AA06_ms3_dev()
        #
        # self.click_CD320_AA78_ms5()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD320_AA78_ms5()
        #
        # self.click_CD310_2E51_ms4_dev()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD310_2E51_ms4_dev()
        #
        # self.check_second_tree()
        #
        # time.sleep(2)
        #
        # self.click_CD100_E772_ms4()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD100_E772_ms4()
        #
        # self.click_N1001_3A00_bwd()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_N1001_3A00_bwd()
        #
        # self.click_CD600_EF78_ms6_serv()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD600_EF78_ms6_serv()
        #
        # self.click_CD100_E778_ms5()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD100_E778_ms5()
        #
        # self.click_CD100_E75A_ms3_dev()
        # self.open_schedule_open_archive()
        # time.sleep(4)
        # self.check_camera_CD100_E75A_ms3_dev()

        self.app.logout_butten()

    def click_yesterday(self):
        driver = self.app.driver
        now = datetime.datetime.now()
        cur_day = now.day
        self.strg_today = now.strftime('%B %d, %Y')
        yesterday = str(cur_day - 1)
        time.sleep(4)
        driver.find_element_by_xpath('//div[@class="item day" and contains(text(), "' + yesterday + '")]').click()

    def open_schedule_open_archive(self):
        driver = self.app.driver
        self.app.Schedule.open_schedule()
        time.sleep(3)
        self.app.Schedule.yesterday_day_of_the_week()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="navigation"]/table/tbody/tr/td[2]/a').click()
        self.click_yesterday()

    def schedule_camera(self):
        driver = self.app.driver
        self.app.Schedule.open_schedule()
        time.sleep(5)
        self.app.Schedule.item_time()
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[3]/div[2]/ul/li/ul")))

    #Камеры для проверке на рабочем сервере
    def click_CD100_E75A_ms3_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12597"]/a').click()  # камера CD100(E75A)_ms3_dev
        self.camera_name = self.title()

    def click_CD100_E778_ms5(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_6827"]/a').click()  # камера CD100(E778)_ms5_ПЗ
        self.camera_name = self.title()

    def click_CD600_EF78_ms6_serv(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12601"]/a').click()  # камера CD600(EF78)_ms6_serv
        self.camera_name = self.title()

    def click_N1001_3A00_bwd(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_14875"]/a').click()  # камера N1001(3A00)_bwd
        self.camera_name = self.title()

    def click_CD100_E772_ms4(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_6830"]/a').click()  # камера CD100(E772)_ms4_ПЗ
        self.camera_name = self.title()

    def click_CD310_2E51_ms4_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_13959"]/a').click()  # камера CD310(2E51)_ms4_dev
        self.camera_name = self.title()

    def click_CD320_AA78_ms5(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_11460"]/a').click()  # камера CD320(AA78)_ms5_Пр_С
        self.camera_name = self.title()

    def click_CD320_AA06_ms3_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12603"]/a').click()  # камера CD320(AA06)_ms3_dev
        self.camera_name = self.title()

    def click_CD630_910D_ms6_dev(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12602"]/a').click()  # камера CD630(910D)_ms6_dev
        self.camera_name = self.title()

    #Камеры для проверки на тестовом сервере
    def click_CD_120(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_4343"]/a').click()
        self.camera_name = self.title()

    def click_CD120_D521(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_4184"]/a').click()
        self.camera_name = self.title()

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

    #Камеры для проверке на рабочем сервере
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

    #Камеры для проверки на тестовом сервере
    def check_camera_CD_120(self):
        self.archive_check()

    def check_camera_CD120_D521(self):
        self.archive_check()

    def archive_check(self):
        self.app.LineHours.check_time_0()
        self.app.LineHours.check_time_1()
        self.app.LineHours.check_time_2()
        self.app.LineHours.check_time_3()
        self.app.LineHours.check_time_4()
        self.app.LineHours.check_time_5()
        self.app.LineHours.check_time_6()
        self.app.LineHours.check_time_7()
        self.app.LineHours.check_time_8()
        self.app.LineHours.check_time_9()
        self.app.LineHours.check_time_10()
        self.app.LineHours.check_time_11()
        self.app.LineHours.check_time_12()
        self.app.LineHours.check_time_13()
        self.app.LineHours.check_time_14()
        self.app.LineHours.check_time_15()
        self.app.LineHours.check_time_16()
        self.app.LineHours.check_time_17()
        self.app.LineHours.check_time_18()
        self.app.LineHours.check_time_19()
        self.app.LineHours.check_time_20()
        self.app.LineHours.check_time_21()
        self.app.LineHours.check_time_22()
        self.app.LineHours.check_time_23()

# TODO : РЕФАКТОРИНГ - Сделать проверку плеера. Добавить наведение фокуса на тамлайн, чтобы считать дилу видео

    def check_player(self):
        driver = self.app.driver
        try:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.hover-video')))
            try:
                width_element = 0
                while width_element < 7:
                    time.sleep(1)
                    T = driver.find_element_by_css_selector('div.player-bottom-controlbar-progress-left')
                    size_element = T.size
                    width_element = size_element['width']
                self.focus_element()
                self.seek_total_time()
                self.video_length_check()
            except TimeoutException:
                self.text_the_video_did_not_load()
        except TimeoutException:
            self.text_player_is_not_displayed()

    def text_player_is_not_displayed(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Плеер под номером ' + str(
                self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" не отобразился.')
        with open('monitoring error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.strg_today + '" WARNING: Проверка для камеры "' + self.camera_name.strip() + '" выполнена. Плеер под номером ' + str(
                    self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" не отобразился.\n')
            f.close()

    def text_the_video_did_not_load(self):
        driver = self.app.driver
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Видео под номером ' + str(
                self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" не загрузилось')
        with open('monitoring error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.strg_today + '" WARNING: Проверка для камеры "' + self.camera_name.strip() + '" выполнена. Видео под номером ' + str(
                    self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" не загрузилось.\n')
            f.close()
        driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()

    def video_length_check(self):
        # Проверка длительности записи Архива
        driver = self.app.driver
        if str(self.archive_time) > '11:50':
            print(
                'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео под номером ' + str(
                    self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" загрузилось. Длительность видео ' + str(
                    self.archive_time).strip() + ' минут.')

            with open('monitoring report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"' + self.strg_today + '" INFO: Проверка для камеры "' + self.camera_name.strip() + '" выполнена. Видео под номером ' + str(
                        self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" загрузилось. Длительность видео ' + str(
                        self.archive_time).strip() + ' минут.\n')
                f.close()
        else:
            print(
                'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео под номером ' + str(
                    self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" загрузилось. Длительность видео ' + str(
                    self.archive_time) + ' минут. !Длительность Архива меньше допустимой!')

            with open('monitoring error report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"' + self.strg_today + '" WARNING: Проверка для камеры "' + self.camera_name.strip() + '" выполнена. Видео под номером ' + str(
                        self.app.LineHours.ii) + ' за временной диапазон "' + self.app.LineHours.time_name.strip() + ' часов" загрузилось. Длительность видео ' + str(
                        self.archive_time).strip() + ' минут. !Длительность Архива меньше допустимой!\n')
                f.close()
        driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()

    def seek_total_time(self):
        driver = self.app.driver
        archive_duration = driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[2]')
        self.archive_time = archive_duration.get_attribute('textContent')
        return self.archive_time

    def focus_element(self):
        driver = self.app.driver
        Focus = ActionChains(driver)
        Focus.move_to_element(driver.find_element_by_css_selector('div.player-bottom-controlbar')).perform()


    def title(self):
        driver = self.app.driver
        camera_title = driver.find_element_by_css_selector('a.jstree-clicked')
        camera_name = camera_title.get_attribute('textContent')
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

#TODO : Сделать проверку на наличие txt файлов в папке test
    def delete_txt(self):
        T = Path('.').glob('*.txt')
        for f in T:
            Path.unlink(f)

