import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TopEditButtons:

    def __init__(self, app):
        self.app = app

    def add_camera_player1(self):
        driver = self.app.driver
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lpanel"]/div[1]')))
        driver.find_element_by_xpath('//*[@id="screen_1"]').click()
        #Проверка добавления камеры в Плеер 1
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]')
            self.app.MessagesForTheReport.player1_added()
        except NoSuchElementException:
            self.app.MessagesForTheReport.no_player1_added()

    def add_camera_player2(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_2"]').click()
        #Проверка добавления камеры в Плеер 2
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[2]/div/div[2]')
            self.app.MessagesForTheReport.player2_added()
        except NoSuchElementException:
            self.app.MessagesForTheReport.no_player2_added()

    def add_camera_player3(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_3"]').click()
        #Проверка добавления камеры в Плеер 3
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[3]/div/div[2]')
            self.app.MessagesForTheReport.player3_added()
        except NoSuchElementException:
            self.app.MessagesForTheReport.no_player3_added()

    def add_camera_player4(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="screen_4"]').click()
        #Проверка добавления камеры в Плеер 4
        try:
            driver.find_element_by_xpath('//*[@id="screens"]/div[4]/div/div[2]')
            self.app.MessagesForTheReport.player4_added()
        except NoSuchElementException:
            self.app.MessagesForTheReport.no_player4_added()

    def add_camera_button(self):
        driver = self.app.driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#" and contains(text(), "' + self.app.Monitoring.camera_name.strip() + '")]')))
        driver.find_element_by_xpath('//*[@id="activation-device"]').click()
        #Проверка, что открылась Форма добавления камеры
        if driver.find_element_by_xpath(
                '//*[@id="body"]/div[1]').text == "Форма добавления камеры":
            driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[3]/input[1]').click()
            self.app.MessagesForTheReport.camera_add_form_is_open()
        else:
            self.app.MessagesForTheReport.camera_add_form_is_not_open()

    def camera_delete_button(self):
        driver = self.app.driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#" and contains(text(), "' + self.app.Monitoring.camera_name.strip() + '")]')))
        driver.find_element_by_xpath('//*[@id="deactivation-device"]').click()
        #Проверка, что открылась Форма удаления камеры
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body"]/div[1]')))
        if driver.find_element_by_xpath(
                '//*[@id="body"]/div[1]').text == "Форма удаления камеры":
            self.app.MessagesForTheReport.camera_delete_form_is_open()
        else:
            self.app.MessagesForTheReport.camera_delete_form_is_not_open()

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
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#" and contains(text(), "' + self.app.Monitoring.camera_name.strip() + '")]')))
        old_name_camera = driver.find_element_by_xpath('//a[@href="#" and contains(text(), "' + self.app.Monitoring.camera_name.strip() + '")]').text
        driver.find_element_by_xpath('//*[@id="rename-channel"]').click()
        rename_camera = driver.find_element_by_css_selector('input.jstree-rename-input')
        time.sleep(1)
        rename_camera.send_keys('test_name')
        time.sleep(1)
        rename_camera.send_keys(Keys.ENTER)
        new_name_camera = driver.find_element_by_class_name('jstree-clicked').text
        # Проверка, что изменилось имя камеры
        if new_name_camera != old_name_camera:
            self.app.MessagesForTheReport.camera_renamed()
            if 'test_name' in new_name_camera:
                self.app.TopEditButtons.camera_rename_CD120_D521()
        else:
            self.app.MessagesForTheReport.camera_not_renamed()
