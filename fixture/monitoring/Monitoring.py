import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Monitoring:

    def __init__(self, app):
        self.app = app

    def click_yesterday(self):
        driver = self.app.driver
        self.app.DateDetermination.find_yesterday()
        time.sleep(4)
        try:
            #Если "сегодняшний день" равен 1, то проверяется сколько было дней в прошлом месяце и переключатся календарь на тот месяц и выбирается последний день
            if self.app.DateDetermination.present_day == 1:
                self.app.DateDetermination.find_previous_month()
                driver.find_element_by_xpath('//*[@id="calendar"]/table/tbody/tr[1]/th[1]').click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '//div[@class="item day" and contains(text(), "' + self.app.DateDetermination.number_of_days + '")]')))
                driver.find_element_by_xpath(
                    '//div[@class="item day" and contains(text(), "' + self.app.DateDetermination.number_of_days + '")]').click()
            else:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="item day" and contains(text(), "' + self.app.DateDetermination.yesterday + '")]')))
                driver.find_element_by_xpath('//div[@class="item day" and contains(text(), "' + self.app.DateDetermination.yesterday + '")]').click()
        except:
            self.app.MessagesForTheReport.no_archive_for_the()
            self.app.Authorization.logout_butten()
            self.app.destroy()

    def open_schedule_open_archive(self):
        driver = self.app.driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#" and contains(text(), "' + self.camera_name.strip() + '")]')))
        self.app.Schedule.open_schedule()
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#schedule")))
            self.app.Schedule.yesterday_day_of_the_week()
            self.app.Archive.open_archive()
            self.click_yesterday()
        except TimeoutException:
            print('Не загрузилось расписание')
            self.app.destroy()

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

    def check_player(self):
        driver = self.app.driver
        try:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.container.active')))
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.player-bottom-controlbar-progress-left')))
                width_element = 0 #Переменная для отслеживания длины загруженного таймлайна
                caunter = 0 #Переменная для счетчика отслеживающий загрузку видео
                while width_element < 7 and caunter < 15:
                    time.sleep(1)
                    # print(str(caunter) + ' - счетчик, длина пройденного таймлайна - ' + str(width_element))
                    caunter += 1
                    time_line = driver.find_element_by_css_selector('div.player-bottom-controlbar-progress-left')
                    size_element = time_line.size
                    width_element = size_element['width']
                if width_element == 0:
                    self.app.LineHours.getting_time()
                    self.app.MessagesForTheReport.video_did_not_load_in_15_seconds()
                    driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()
                else:
                    self.focus_element()
                    self.seek_total_time()
                    self.video_length_check()
            except TimeoutException:
                self.app.MessagesForTheReport.Player_did_not_load_in_10_seconds()
        except TimeoutException:
            self.app.LineHours.getting_time()
            self.app.DateDetermination.find_yesterday()
            self.app.MessagesForTheReport.player_did_not_appear_in_15_seconds()

    def video_length_check(self):
        # Проверка длительности записи Архива
        driver = self.app.driver
        if str(self.archive_time) > '11:50':
            # self.app.Requests.request_test()
            self.app.MessagesForTheReport.video_download_and_the_duration_is_correct()
        else:
            if self.app.LineHours.digit_from_the_schedule_array == 2:
                # self.app.Requests.request_test()
                self.app.MessagesForTheReport.motion_recording()
            else:
                if str(self.archive_time) == '00:13':
                    # self.app.Requests.request_test()
                    self.screen_archive()
                    self.app.RMS.computation_rms()
                    if self.app.RMS.rms4 == 0.0:
                        self.app.MessagesForTheReport.maximum_allowed_concurrent_connections_exceeded()
                else:
                    # self.app.Requests.request_test()
                    self.app.MessagesForTheReport.archive_duration_is_shorter()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="screen"]/div[1]/div/div[1]/img')))
        driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[1]/img').click()

    def seek_total_time(self):
        driver = self.app.driver
        archive_duration = driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[2]')
        self.archive_time = archive_duration.get_attribute('textContent')
        print(self.archive_time, ' - время длительности видео архива.')

    def focus_element(self):
        driver = self.app.driver
        focus = ActionChains(driver)
        focus.move_to_element(driver.find_element_by_css_selector('div.player-bottom-controlbar')).perform()

    def title_camera(self):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.jstree-clicked')))
        camera_title = driver.find_element_by_css_selector('a.jstree-clicked')
        self.camera_name = camera_title.get_attribute('textContent')

    def screen_archive(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen"]/div[1]/div/div[2]/div[2]').screenshot("1.png")  # делаем скриншот видеоплеера
        time.sleep(1)