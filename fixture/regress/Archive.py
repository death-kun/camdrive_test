import time
import glob
import os
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ArchiveCheck:

    def __init__(self, app):
        self.app = app

    def open_archive(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="navigation"]/table/tbody/tr/td[2]/a').click()

    def video_archive_fragment_download(self):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='time-intervals']/table/tbody"))) #Ожидание отрисовки таблицы с контейнерами с архивом
        self.date_selection()
        self.timing()
        time.sleep(1)
        self.duration_selection()
        driver.find_element_by_xpath('//*[@id="generate_link"]').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='notification-block']/div[2]"))) #Ожидание появления диалогового окна
        driver.find_element_by_xpath('//*[@id="notification-block"]/div[2]/div[3]/div/button[1]/span').click()

    def duration_selection(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="archive_download"]/div/table/tbody/tr[3]/td[2]/img').click()
        self.coordinate_determination()
        Minutes = driver.find_element_by_xpath('//*[@id="ui_tpicker_minute_downloadduration"]/a')
        ActionChains(driver).drag_and_drop_by_offset(Minutes, self.Mx, 1).perform()
        driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[3]/button[2]').click()

    def timing(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="archive_download"]/div/table/tbody/tr[2]/td[2]/img').click()
        self.coordinate_determination()
        hour = driver.find_element_by_xpath('//*[@id="ui_tpicker_hour_downloadtime"]/a')
        ActionChains(driver).drag_and_drop_by_offset(hour, self.hx, 1).perform()
        minutes = driver.find_element_by_xpath('//*[@id="ui_tpicker_minute_downloadtime"]/a')
        ActionChains(driver).drag_and_drop_by_offset(minutes, self.mx, 1).perform()
        element = driver.find_element_by_css_selector('dd#ui_tpicker_time_downloadtime.ui_tpicker_time')
        element_time_timing = element.get_attribute('textContent')
        time_timing = list(element_time_timing)
        time_timing[2] = '_'
        self.attribute_time_timing = "".join(time_timing)
        driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[3]/button[2]').click()


    def coordinate_determination(self):
        driver = self.app.driver
        win = driver.find_element_by_xpath('//*[@id="wrapper"]')
        size_element = win.size
        width_element = size_element['width']
        self.hx = (int(width_element) * 2) / 100  # Для определения движения бегунка для Часов в Выборе времени
        self.mx = (int(width_element) * 1) / 100  # Для определения движения бегунка для Минут в Выборе времени
        self.Mx = (int(width_element) * 1) / 100  # Для определения движения бегунка для Минут в Выборе длительности

    def date_selection(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="archive_download"]/div/table/tbody/tr[1]/td[2]/img').click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody")))
        self.app.DateDetermination.find_yesterday()
        driver.find_element_by_xpath(
            '//*[@class="ui-state-default" and contains(text(), "' + self.app.DateDetermination.yesterday + '")]').click()

    def search_avi(self):
        counter = 0
        while counter != 1:
            PATH = os.path.expanduser('~\Downloads')
            filelist = glob.glob(os.path.join(PATH, "*.avi"))
            for f in filelist:
                print(f)
                self.avi_file = Path(f).name #Файл, который скачался
                print('Файл, который скачался', self.avi_file)
                print('Проверка, что скачался видеофайл архива. Проверка прошла успешно. Файл скачался.')
                counter += 1
                m_Y_element = self.app.DateDetermination.now.strftime('%m_%Y') #Определяем месяц и год
                if int(self.app.DateDetermination.yesterday) < 10:
                    file_name = '' + self.app.Monitoring.camera_name.strip() + '_0' + self.app.DateDetermination.yesterday + '_' + m_Y_element + '_' + self.attribute_time_timing + '.avi' #Файл, который мы ищем
                    print('Файл, который мы ищем', file_name)
                else:
                    file_name = '' + self.app.Monitoring.camera_name.strip() + '_' + self.app.DateDetermination.yesterday + '_' + m_Y_element + '_' + self.attribute_time_timing + '.avi' #Файл, который мы ищем
                    print('Файл, который мы ищем', file_name)
                if file_name == self.avi_file:
                    self.app.MessagesForTheReport.download_the_desired_archive_file()
                else:
                    self.app.MessagesForTheReport.wrong_archive_file_downloaded()

    def delete_avi(self):
        PATH = os.path.expanduser('~/Downloads')
        filelist = glob.glob(os.path.join(PATH, "*.avi"))
        for f in filelist:
            os.remove(f)
            print('Все avi файлы удалены из папки Загрузки.')