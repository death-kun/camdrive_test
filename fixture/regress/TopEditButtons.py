import time
from selenium.webdriver.common.keys import Keys

class top_edit_buttons:

    def __init__(self, app):
        self.app = app

    def add_camera_button(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="activation-device"]').click()
        #Проверка, что открылась Форма добавления камеры
        if driver.find_element_by_xpath(
                '//*[@id="body"]/div[1]').text == "Форма добавления камеры":
            print('Проверка, что открылась Форма добавления камеры. Проверка прошла успешно. Открылась Форма добавления камеры')
            self.app.logout_butten()
        else:
            print('Проверка, что открылась Форма добавления камеры. Проверка провалилась. Не открылась Форма добавления камеры')
            self.app.logout_butten()

    def remove_camera_button(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        driver.find_element_by_xpath('//*[@id="deactivation-device"]').click()
        time.sleep(1)
        #Проверка, что открылась Форма удаления камеры
        if driver.find_element_by_xpath(
                '//*[@id="body"]/div[1]').text == "Форма удаления камеры":
            print(
                'Проверка, что открылась Форма удаления камеры. Проверка прошла успешно. Открылась Форма удаления камеры')
            self.app.logout_butten()
        else:
            print(
                'Проверка, что открылась Форма удаления камеры. Проверка провалилась. Не открылась Форма удаления камеры')
            self.app.logout_butten()

    def camera_rename_button(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        old_name_camera = driver.find_element_by_xpath('//*[@id="node_4184"]/a').text
        self.camera_rename_test_name()
        new_name_camera = driver.find_element_by_xpath('//*[@id="node_4184"]/a').text
        #Проверка, что изменилось имя камеры
        if new_name_camera != old_name_camera:
            print('Проверка, что изменилось имя камеры. Проверка прошла успешно. Камера переименована')
            if 'test_name' in new_name_camera:
                self.camera_rename_CD120_D521()
                self.app.logout_butten()
        else:
            print('Проверка, что изменилось имя камеры. Проверка провалилась. Камера не переименована')
            self.app.logout_butten()

    def camera_rename_CD120_D521(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="rename-channel"]').click()
        rename_camera = driver.find_element_by_css_selector('input.jstree-rename-input')
        time.sleep(1)
        rename_camera.send_keys('CD120_D521')
        time.sleep(1)
        rename_camera.send_keys(Keys.ENTER)

    def camera_rename_test_name(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="rename-channel"]').click()
        rename_camera = driver.find_element_by_css_selector('input.jstree-rename-input')
        time.sleep(1)
        rename_camera.send_keys('test_name')
        time.sleep(1)
        rename_camera.send_keys(Keys.ENTER)