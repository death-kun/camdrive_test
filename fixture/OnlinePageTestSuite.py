import time
import glob, os
from selenium.common.exceptions import NoSuchElementException

class onlineTestSuite:

    def __init__(self, app):
        self.app = app

    def add_camera_player1(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="screen_1"]').click()
        #Проверка добавления камеры в Плеер 1
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]')
            print('Проверка добавления камеры в Плеер 1. Проверка прошла успешно. Добавлена камера в Плеер 1')
            cross_button = driver.find_element_by_css_selector('img.iePNG.ch.screen-close')
            cross_button.click()
            self.app.logout_butten()
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 1. Проверка провалилась.Камера не добавлена в Плеер 1')
            self.app.logout_butten()

    def add_camera_player2(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="screen_2"]').click()
        #Проверка добавления камеры в Плеер 2
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[2]/div/div[2]')
            print('Проверка добавления камеры в Плеер 2. Проверка прошла успешно. Добавлена камера в Плеер 2')
            cross_button = driver.find_element_by_css_selector('img.iePNG.ch.screen-close')
            cross_button.click()
            self.app.logout_butten()
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 2. Проверка провалилась. Камера не добавлена в Плеер 2')
            self.app.logout_butten()

    def add_camera_player3(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="screen_3"]').click()
        #Проверка добавления камеры в Плеер 3
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[3]/div/div[2]')
            print('Проверка добавления камеры в Плеер 3. Проверка прошла успешно. Добавлена камера в Плеер 3')
            cross_button = driver.find_element_by_css_selector('img.iePNG.ch.screen-close')
            cross_button.click()
            self.app.logout_butten()
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 3. Проверка провалилась. Камера не добавлена в Плеер 3')
            self.app.logout_butten()

    def add_camera_player4(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="screen_4"]').click()
        #Проверка добавления камеры в Плеер 4
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[4]/div/div[2]')
            print('Проверка добавления камеры в Плеер 4. Проверка прошла успешно. Добавлена камера в Плеер 4')
            cross_button = driver.find_element_by_css_selector('img.iePNG.ch.screen-close')
            cross_button.click()
            self.app.logout_butten()
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 4. Проверка провалилась. Камера не добавлена в Плеер 4')
            self.app.logout_butten()

    def archive_search(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        #Проверка, что появился новый день с архивом
        try:
            driver.find_element_by_css_selector('div.item.day.today')
            print('Проверка, что появился новый день с архивом. Проверка прошла успешно. Найден архив за текущий день')
            self.app.logout_butten()
        except NoSuchElementException:
            print('Проверка, что появился новый день с архивом. Проверка провалилась. Архив за текущий день не найден')
            self.app.logout_butten()

    def archive_playback(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        self.open_archive()
        #Проверка, что открылся плеер с архивом
        try:
            driver.find_element_by_css_selector('div.hover-video')
            print('Проверка, что открылся плеер с архивом. Проверка прошла успешно. Плеер с архивом открыт')
            self.app.logout_butten()
        except NoSuchElementException:
            print('Проверка, что открылся плеер с архивом. Проверка провалилась. Плеер с архивом не открыт')
            self.app.logout_butten()

    def open_archive(self):
        driver = self.app.driver
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        driver.find_element_by_css_selector('div.item.day.today').click()
        time.sleep(1)
        click_element = driver.find_element_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant"]')
        time.sleep(1)
        click_element.click()
        time.sleep(2)

    def download_archive(self):
        driver = self.app.driver

        #Проверка есть ли в папке Downloads файл с расширением avi и удаляет его
        PATH = os.path.expanduser('~/Downloads')
        filelist = glob.glob(os.path.join(PATH, "*.avi"))
        for f in filelist:
            os.remove(f)
            print('Файл удален')

        self.app.open_home_page()
        self.app.login_autotest()
        self.open_archive()
        button_dowload = driver.find_element_by_xpath('//*[@id="generate_link"]')
        time.sleep(1)
        button_dowload.click()
        time.sleep(2)
        button_OK = driver.find_element_by_xpath('//*[@id="notification-block"]/div[2]/div[3]/div/button[1]/span')
        time.sleep(1)
        button_OK.click()

        time.sleep(60) #Время на скачивание файла

        #Проверка, что скачался видеофайл архива
        os.chdir(os.path.expanduser('~/Downloads'))
        if glob.glob('*.avi'):
            print(glob.glob('*.avi'))
            print('Проверка, что скачался видеофайл архива. Проверка прошла успешно. Файл скачался')
            self.app.logout_butten()
        else:
            print('Проверка, что скачался видеофайл архива. Проверка провалилась.Файл не скачался')
            self.app.logout_butten()



