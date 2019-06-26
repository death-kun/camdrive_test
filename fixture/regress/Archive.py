import time
import glob, os
from selenium.common.exceptions import NoSuchElementException

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

#TODO :: Сделать Рефакторинг. Добавить создание отчета. Таймаут для ожидания скачивания файла заменить на проверку/ожидание
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
        time.sleep(90) #Время на скачивание файла
        #Проверка, что скачался видеофайл архива
        os.chdir(os.path.expanduser('~/Downloads'))
        if glob.glob('*.avi'):
            print(glob.glob('*.avi'))
            print('Проверка, что скачался видеофайл архива. Проверка прошла успешно. Файл скачался')
            self.app.logout_butten()
        else:
            print('Проверка, что скачался видеофайл архива. Проверка провалилась.Файл не скачался')
            self.app.logout_butten()