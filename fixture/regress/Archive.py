import time
import glob
import os
from pathlib import PurePath
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class archive_check:

    def __init__(self, app):
        self.app = app

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

    def open_archive(self):
        driver = self.app.driver
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()

#TODO :: Сделать Рефакторинг. Добавить создание отчета. Таймаут для ожидания скачивания файла заменить на проверку/ожидание
    def download_archive(self):
        driver = self.app.driver

        #Проверка есть ли в папке Downloads файл с расширением avi и удаляет его
        PATH = os.path.expanduser('~/Downloads')
        filelist = glob.glob(os.path.join(PATH, "*.avi"))
        for f in filelist:
            os.remove(f)
            print('Файл удален')

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='time-intervals']/table/tbody"))) #Ожидание отрисовки таблицы с контейнерами с архивом

        driver.find_element_by_xpath('//*[@id="generate_link"]').click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='notification-block']/div[2]"))) #Ожидание появления диалогового окна

        driver.find_element_by_xpath('//*[@id="notification-block"]/div[2]/div[3]/div/button[1]/span').click()

        # Проверка, что скачался видеофайл архива
        T = 0
        while T != 1:
            PATH = os.path.expanduser('~/Downloads')
            filelist = glob.glob(os.path.join(PATH, "*.avi"))
            for f in filelist:
                print(f)
                print('Проверка, что скачался видеофайл архива. Проверка прошла успешно. Файл скачался')
                T += 1
