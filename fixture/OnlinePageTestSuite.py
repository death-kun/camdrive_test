import time
import random
from selenium.common.exceptions import NoSuchElementException


class onlineTestSuite:

    def __init__(self, app):
        self.app = app

    def add_camera_player1(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        #Проверка добавления камеры в Плеер 1
        if driver.find_element_by_css_selector('div.container:nth-child(1)').is_displayed():
            driver.find_element_by_xpath('//*[@id="screen_1"]').click()
            if driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]').is_displayed():
                print('Проверка добавления камеры в Плеер 1. Проверка прошла успешно. Добавлена камера в Плеер 1')
                self.app.logout_butten()
            else:
                print('Проверка добавления камеры в Плеер 1. Проверка провалилась.Камера не добавлена в Плеер 1')
                self.app.logout_butten()

    def add_camera_player2(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        # Проверка добавления камеры в Плеер 2
        if driver.find_element_by_css_selector('div.container.s.num-2').is_displayed():
            driver.find_element_by_xpath('//*[@id="screen_2"]').click()
            if driver.find_element_by_xpath('//*[@id="screens"]/div[2]/div/div[2]').is_displayed():
                print('Проверка добавления камеры в Плеер 2. Проверка прошла успешно. Добавлена камера в Плеер 2')
                self.app.logout_butten()
            else:
                print('Проверка добавления камеры в Плеер 2. Проверка провалилась. Камера не добавлена в Плеер 2')
                self.app.logout_butten()

    def add_camera_player3(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        # Проверка добавления камеры в Плеер 3
        if driver.find_element_by_css_selector('div.container.s.num-3').is_displayed():
            driver.find_element_by_xpath('//*[@id="screen_3"]').click()
            if driver.find_element_by_xpath('//*[@id="screens"]/div[3]/div/div[2]').is_displayed():
                print('Проверка добавления камеры в Плеер 3. Проверка прошла успешно. Добавлена камера в Плеер 3')
                self.app.logout_butten()
            else:
                print('Проверка добавления камеры в Плеер 3. Проверка провалилась. Камера не добавлена в Плеер 3')
                self.app.logout_butten()

    def add_camera_player4(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        # Проверка добавления камеры в Плеер 4
        if driver.find_element_by_css_selector('div.container.s.num-4').is_displayed():
            driver.find_element_by_xpath('//*[@id="screen_4"]').click()
            if driver.find_element_by_xpath('//*[@id="screens"]/div[4]/div/div[2]').is_displayed():
                print('Проверка добавления камеры в Плеер 4. Проверка прошла успешно. Добавлена камера в Плеер 4')
                self.app.logout_butten()
            else:
                print('Проверка добавления камеры в Плеер 4. Проверка провалилась. Камера не добавлена в Плеер 4')
                self.app.logout_butten()

    def archive_search(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        #Проверка, что появился новый день с архивом
        if driver.find_element_by_css_selector('div.item.day.today').is_displayed():
            print('Проверка, что появился новый день с архивом. Проверка прошла успешно. Найден архив за текущий день')
            self.app.logout_butten()
        else:
            print('Проверка, что появился новый день с архивом. Проверка провалилась. Архив за текущий день не найден')
            self.app.logout_butten()

    def archive_playback(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        driver.find_element_by_css_selector('div.item.day.today').click()

        # element = driver.find_elements_by_css_selector('div.time.item.constant')
        # # list_archive = [element]
        # # random_element = random.choice(list_archive)
        # # random_element.click()
        # click_element = driver.find_element_by_class_name("time item  constant")
        # driver.execute_script("arguments[0].click();", click_element)
        # javaScript = "document.querySelector('div.time.item.constant')[0].click();"
        # driver.execute_script(javaScript)
        # driver.find_element_by_class_name('time item  constant').click

        driver.find_element_by_xpath('//*[@id="1"]/td[2]').click()
        time.sleep(10)
        
        #Проверка, что открылся плеер с архивом
        try:
            driver.find_element_by_css_selector('div.hover-video')
            print('Плеер с архивом открыт')
            self.app.logout_butten()

        except NoSuchElementException:
            print('Плеер с архивом не открыт')
            self.app.logout_butten()
