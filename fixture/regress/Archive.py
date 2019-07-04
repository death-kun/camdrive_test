import time
import glob
import os
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class archive_check:

    def __init__(self, app):
        self.app = app

    def open_archive(self):
        driver = self.app.driver
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()

#TODO :: Сделать Рефакторинг. Добавить создание отчета. Таймаут для ожидания скачивания файла заменить на проверку/ожидание
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
        self.app.Monitoring.find_yesterday()
        driver.find_element_by_xpath(
            '//*[@class="ui-state-default" and contains(text(), "' + self.app.Monitoring.yesterday + '")]').click()

    def search_avi(self):
        T = 0
        while T != 1:
            PATH = os.path.expanduser('~\Downloads')
            filelist = glob.glob(os.path.join(PATH, "*.avi"))

            for f in filelist:
                print(f)
                avi = Path(f).name #Файл, который скачался
                print('Файл, который скачался', avi) 
                print('Проверка, что скачался видеофайл архива. Проверка прошла успешно. Файл скачался.')
                T += 1
                m_Y_element = self.app.Monitoring.now.strftime('%m_%Y')

                if int(self.app.Monitoring.yesterday) < 10:
                    camer_name = '' + self.app.Monitoring.camera_name.strip() + '_0' + self.app.Monitoring.yesterday + '_' + m_Y_element + '_' + self.attribute_time_timing + '.avi' #Файл, который мы ищем
                    print('Файл, который мы ищем', camer_name)
                else:
                    camer_name = '' + self.app.Monitoring.camera_name.strip() + '_' + self.app.Monitoring.yesterday + '_' + m_Y_element + '_' + self.attribute_time_timing + '.avi' #Файл, который мы ищем
                    print('Файл, который мы ищем', camer_name)

                if camer_name == avi:
                    print('Скачался нужный файл.')
                    with open('download archive report.txt', 'a', encoding='utf-8') as f:
                        f.write(
                            '"' + self.app.Monitoring.strg_today + '" "Проверка скачивания Архива" INFO: Проверка выполнена. Архив ' + str(avi) + ' скачался.\n')
                        f.close()
                else:
                    print("Скачался не тот файл.")
                    with open('download archive error report.txt', 'a', encoding='utf-8') as f:
                        f.write(
                            '"' + self.app.Monitoring.strg_today + '" "Проверка скачивания Архива" WARNING: Проверка выполнена. Архив ' + str(avi) + ' не скачался.\n')
                        f.close()


    def delete_avi(self):
        PATH = os.path.expanduser('~/Downloads')
        filelist = glob.glob(os.path.join(PATH, "*.avi"))
        for f in filelist:
            os.remove(f)
            print('Все avi файлы удалены из папки Загрузки.')
