import time
from selenium.webdriver.common.keys import Keys

class top_edit_buttons:

    def __init__(self, app):
        self.app = app

    def add_camera_button(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="activation-device"]').click()
        #Проверка, что открылась Форма добавления камеры
        if driver.find_element_by_xpath(
                '//*[@id="body"]/div[1]').text == "Форма добавления камеры":
            print('Проверка, что открылась Форма добавления камеры. Проверка прошла успешно. Открылась Форма добавления камеры')
        else:
            print('Проверка, что открылась Форма добавления камеры. Проверка провалилась. Не открылась Форма добавления камеры')

    def remove_camera_button(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="deactivation-device"]').click()
        #Проверка, что открылась Форма удаления камеры
        if driver.find_element_by_xpath(
                '//*[@id="body"]/div[1]').text == "Форма удаления камеры":
            print(
                'Проверка, что открылась Форма удаления камеры. Проверка прошла успешно. Открылась Форма удаления камеры')
        else:
            print(
                'Проверка, что открылась Форма удаления камеры. Проверка провалилась. Не открылась Форма удаления камеры')


    def camera_rename_CD120_D521(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="rename-channel"]').click()
        rename_camera = driver.find_element_by_css_selector('input.jstree-rename-input')
        time.sleep(1)
        rename_camera.send_keys('CD120_D521')
        time.sleep(1)
        rename_camera.send_keys(Keys.ENTER)

    def camera_rename_button(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="rename-channel"]').click()
        rename_camera = driver.find_element_by_css_selector('input.jstree-rename-input')
        time.sleep(1)
        rename_camera.send_keys('test_name')
        time.sleep(1)
        rename_camera.send_keys(Keys.ENTER)