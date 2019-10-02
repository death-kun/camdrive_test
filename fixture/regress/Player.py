import time
from selenium.common.exceptions import NoSuchElementException

class PlayerCheck:
    def __init__(self, app):
        self.app = app

    def closing_player(self):
        driver = self.app.driver
        cross_button = driver.find_element_by_css_selector('img.iePNG.ch.screen-close')
        cross_button.click()

    def expand_screen_button(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_1"]').click()
        time.sleep(1)
        self.expand_screen()
        #Проверка, что плеер открылся в формате 1х1
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]')
            print('Проверка, что плеер открылся в формате 1х1. Проверка прошла успешно. Плеер развернулся в Формате 1х1')
        except NoSuchElementException:
            print('Проверка, что плеер открылся в формате 1х1. Проверка провалилась. Плеер не развернулся')

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