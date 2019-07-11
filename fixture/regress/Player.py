import time
from selenium.common.exceptions import NoSuchElementException

class player_check:
    def __init__(self, app):
        self.app = app

    def add_camera_player1(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_1"]').click()
        #Проверка добавления камеры в Плеер 1
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]')
            print('Проверка добавления камеры в Плеер 1. Проверка прошла успешно. Добавлена камера в Плеер 1')
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 1. Проверка провалилась.Камера не добавлена в Плеер 1')

    def add_camera_player2(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_2"]').click()
        #Проверка добавления камеры в Плеер 2
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[2]/div/div[2]')
            print('Проверка добавления камеры в Плеер 2. Проверка прошла успешно. Добавлена камера в Плеер 2')
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 2. Проверка провалилась. Камера не добавлена в Плеер 2')

    def add_camera_player3(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_3"]').click()
        #Проверка добавления камеры в Плеер 3
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[3]/div/div[2]')
            print('Проверка добавления камеры в Плеер 3. Проверка прошла успешно. Добавлена камера в Плеер 3')
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 3. Проверка провалилась. Камера не добавлена в Плеер 3')

    def add_camera_player4(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_4"]').click()
        #Проверка добавления камеры в Плеер 4
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[4]/div/div[2]')
            print('Проверка добавления камеры в Плеер 4. Проверка прошла успешно. Добавлена камера в Плеер 4')
        except NoSuchElementException:
            print('Проверка добавления камеры в Плеер 4. Проверка провалилась. Камера не добавлена в Плеер 4')

    def closing_player(self):
        driver = self.app.driver
        cross_button = driver.find_element_by_css_selector('img.iePNG.ch.screen-close')
        cross_button.click()

    def expand_screen_button(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="screen_1"]').click()
        time.sleep(1)
        self.expand_screen()
        #Проверка, что плеер открылся в формате 1х1
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]')
            print('Проверка, что плеер открылся в формате 1х1. Проверка прошла успешно. Плеер развернулся в Формате 1х1')
            self.closing_player()
            self.app.Authorization.logout_butten()
        except NoSuchElementException:
            print('Проверка, что плеер открылся в формате 1х1. Проверка провалилась. Плеер не развернулся')
            self.app.Authorization.logout_butten()

    def roll_up_screen_button(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="screen_1"]').click()
        time.sleep(1)
        self.expand_screen()
        time.sleep(1)
        self.roll_up_screen()
        #Проверка, что плеер открылся в формате 1х4
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]')
            print('Проверка, что плеер открылся в формате 1х4. Проверка прошла успешно. Плеер развернулся в Формате 1х4')
            self.closing_player()
            self.app.Authorization.logout_butten()
        except NoSuchElementException:
            print('Проверка, что плеер открылся в формате 1х4. Проверка провалилась. Плеер не свернулся')
            self.app.Authorization.logout_butten()

    def roll_up_screen(self):
        driver = self.app.driver
        roll_up_button = driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[1]/div[2]/img[3]')
        time.sleep(1)
        roll_up_button.click()
        time.sleep(2)

    def expand_screen(self):
        driver = self.app.driver
        expand_button = driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[1]/div[2]/img[2]')
        time.sleep(1)
        expand_button.click()
        time.sleep(2)