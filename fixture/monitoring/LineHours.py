
class Hours:

    def __init__(self, app):
        self.app = app

    def check_time_0(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [0, 1, 2, 3, 4]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            # interval = driver.find_elements_by_xpath('//div[@id="time-intervals"]//td//input[@name="interval" and @type="hidden"]')[i]
            # self.interval_value = interval.get_attribute('value') #Получаем интервел, за который просматриваем архив камеры
            # print(self.interval_value)
            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[0], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[0]
            item = driver.find_element_by_xpath('//*[@id="1"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def LIST_INDEX_OUT_OF_RANGE(self, driver, i):
        list_elements = driver.find_elements_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')
        print(list_elements, ' длина списка контейнеров с архивом.')
        len_list_elements = len(list_elements)
        print(i,
              ' - инедекс, который подставляем в для поиска контейнера с архивом')  # Выводим индекс, чтобы отследить ошибку list index out of range
        with open('выявления ошибки LIST INDEX OUT OF RANGE ' + self.app.Monitoring.camera_name.strip() + '.txt',
                  'a',
                  encoding='utf-8') as f:
            f.write(''+ str(i) +' - инедекс, который подставляем в для поиска контейнера с архивом , '+ str(len_list_elements) +' длина списка контейнеров с архивом. \n')
            f.close()

    def check_time_1(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [5, 6, 7, 8, 9]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[1], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[1]
            item = driver.find_element_by_xpath('//*[@id="2"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_2(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [10, 11, 12, 13, 14]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[2], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[2]
            item = driver.find_element_by_xpath('//*[@id="3"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_3(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [15, 16, 17, 18, 19]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[3], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[3]
            item = driver.find_element_by_xpath('//*[@id="4"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_4(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [20, 21, 22, 23, 24]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[4], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[4]
            item = driver.find_element_by_xpath('//*[@id="5"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_5(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [25, 26, 27, 28, 29]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[5], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[5]
            item = driver.find_element_by_xpath('//*[@id="6"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_6(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [30, 31, 32, 33, 34]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[6], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[6]
            item = driver.find_element_by_xpath('//*[@id="7"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_7(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [35, 36, 37, 38, 39]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[7], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[7]
            item = driver.find_element_by_xpath('//*[@id="8"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_8(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [40, 41, 42, 43, 44]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[8], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[8]
            item = driver.find_element_by_xpath('//*[@id="9"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_9(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [45, 46, 47, 48, 49]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[9], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[9]
            item = driver.find_element_by_xpath('//*[@id="10"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_10(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [50, 51, 52, 53, 54]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[10], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[10]
            item = driver.find_element_by_xpath('//*[@id="11"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_11(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [55, 56, 57, 58, 59]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[11], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[11]
            item = driver.find_element_by_xpath('//*[@id="12"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_12(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [60, 61, 62, 63, 64]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[12], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[12]
            item = driver.find_element_by_xpath('//*[@id="13"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_13(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [65, 66, 67, 68, 69]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[13], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[13]
            item = driver.find_element_by_xpath('//*[@id="14"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_14(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [70, 71, 72, 73, 74]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[14], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[14]
            item = driver.find_element_by_xpath('//*[@id="15"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_15(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [75, 76, 77, 78, 79]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[15], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[15]
            item = driver.find_element_by_xpath('//*[@id="16"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_16(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [80, 81, 82, 83, 84]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[16], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[16]
            item = driver.find_element_by_xpath('//*[@id="17"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_17(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [85, 86, 87, 88, 89]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[17], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[17]
            item = driver.find_element_by_xpath('//*[@id="18"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_18(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [90, 91, 92, 93, 94]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[18], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[18]
            item = driver.find_element_by_xpath('//*[@id="19"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_19(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [95, 96, 97, 98, 99]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[19], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[19]
            item = driver.find_element_by_xpath('//*[@id="20"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_20(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [100, 101, 102, 103, 104]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[20], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[20]
            item = driver.find_element_by_xpath('//*[@id="21"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_21(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [105, 106, 107, 108, 109]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[21], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[21]
            item = driver.find_element_by_xpath('//*[@id="22"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_22(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [110, 111, 112, 113, 114]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            self.LIST_INDEX_OUT_OF_RANGE(driver, i)

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[22], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[22]
            item = driver.find_element_by_xpath('//*[@id="23"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_23(self):
        driver = self.app.driver
        self.minutes = 0
        INDEX_LIST = [115, 116, 117, 118, 119]
        for i in INDEX_LIST:

            # Для выявления ошибки LIST INDEX OUT OF RANGE
            list_elements = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')
            print(list_elements)
            with open('выявления ошибки LIST INDEX OUT OF RANGE ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a',
                      encoding='utf-8') as f:
                f.write('"'+ str(list_elements) +'"')
                f.close()
            len_list_elements = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')
            print(len(len_list_elements), ' длина списка контейнеров с архивом.')
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range

            self.archive_container = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[i]
            # print(self.app.Schedule.massiv, ' массив из расписания')                               #Выводим весь массив
            # print(self.app.Schedule.massiv[23], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[23]
            item = driver.find_element_by_xpath('//*[@id="24"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.time_column = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def getting_time(self):
        if self.minutes == 0:
            self.hour_1 = str(self.time_column) + ':' + str(self.minutes) + str('0')
            self.minutes = self.minutes + 12
            self.hour_2 = str(self.time_column) + ':' + str(self.minutes)
            self.hour = self.hour_1 + '-' + self.hour_2
        else:
            self.hour_1 = str(self.time_column) + ':' + str(self.minutes)
            if self.minutes == 48:
                self.minutes = self.minutes + 11
                self.hour_2 = str(self.time_column) + ':' + str(self.minutes)
                self.hour = self.hour_1 + '-' + self.hour_2
            else:
                self.hour_1 = str(self.time_column) + ':' + str(self.minutes)
                self.minutes = self.minutes + 12
                self.hour_2 = str(self.time_column) + ':' + str(self.minutes)
                self.hour = self.hour_1 + '-' + self.hour_2

    def check_for_emptiness(self):
        if "item empty " in self.archive_container.get_attribute('class'):
            item = 0
            if item == self.item_time:
                self.app.Messages_for_the_report.there_is_no_scheduled_archive()
            else:
                self.app.Messages_for_the_report.no_archive()
        else:
            self.archive_container.click()
            self.app.Monitoring.check_player()