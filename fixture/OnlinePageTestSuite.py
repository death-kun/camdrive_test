import time

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

    def click_name_camera(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        time.sleep(1)
        driver.find_element_by_xpath('//li[@id="node_3073"]/a').click()