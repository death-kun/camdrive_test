class hours:

    def __init__(self, app):
        self.app = app

    def check_time_0(self):
        driver = self.app.driver
        self.m = 0
        for i in range(0, 5, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[0], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[0]
            item = driver.find_element_by_xpath('//*[@id="1"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_1(self):
        driver = self.app.driver
        self.m = 0
        for i in range(5, 10, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[1], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[1]
            item = driver.find_element_by_xpath('//*[@id="2"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_2(self):
        driver = self.app.driver
        self.m = 0
        for i in range(10, 15, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[2], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[2]
            item = driver.find_element_by_xpath('//*[@id="3"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_3(self):
        driver = self.app.driver
        self.m = 0
        for i in range(15, 20, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[3], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[3]
            item = driver.find_element_by_xpath('//*[@id="4"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_4(self):
        driver = self.app.driver
        self.m = 0
        for i in range(20, 25, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[4], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[4]
            item = driver.find_element_by_xpath('//*[@id="5"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0] #Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_5(self):
        driver = self.app.driver
        self.m = 0
        for i in range(25, 30, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[5], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[5]
            item = driver.find_element_by_xpath('//*[@id="6"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_6(self):
        driver = self.app.driver
        self.m = 0
        for i in range(30, 35, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[6], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[6]
            item = driver.find_element_by_xpath('//*[@id="7"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_7(self):
        driver = self.app.driver
        self.m = 0
        for i in range(35, 40, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[7], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[7]
            item = driver.find_element_by_xpath('//*[@id="8"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_8(self):
        driver = self.app.driver
        self.m = 0
        for i in range(40, 45, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[8], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[8]
            item = driver.find_element_by_xpath('//*[@id="9"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_9(self):
        driver = self.app.driver
        self.m = 0
        for i in range(45, 50, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[9], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[9]
            item = driver.find_element_by_xpath('//*[@id="10"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_10(self):
        driver = self.app.driver
        self.m = 0
        for i in range(50, 55, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[10], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[10]
            item = driver.find_element_by_xpath('//*[@id="11"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_11(self):
        driver = self.app.driver
        self.m = 0
        for i in range(55, 60, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[11], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[11]
            item = driver.find_element_by_xpath('//*[@id="12"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_12(self):
        driver = self.app.driver
        self.m = 0
        for i in range(60, 65, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[12], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[12]
            item = driver.find_element_by_xpath('//*[@id="13"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_13(self):
        driver = self.app.driver
        self.m = 0
        for i in range(65, 70, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[13], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[13]
            item = driver.find_element_by_xpath('//*[@id="14"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_14(self):
        driver = self.app.driver
        self.m = 0
        for i in range(70, 75, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[14], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[14]
            item = driver.find_element_by_xpath('//*[@id="15"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_15(self):
        driver = self.app.driver
        self.m = 0
        for i in range(75, 80, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[15], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[15]
            item = driver.find_element_by_xpath('//*[@id="16"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_16(self):
        driver = self.app.driver
        self.m = 0
        for i in range(80, 85, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[16], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[16]
            item = driver.find_element_by_xpath('//*[@id="17"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_17(self):
        driver = self.app.driver
        self.m = 0
        for i in range(85, 90, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[17], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[17]
            item = driver.find_element_by_xpath('//*[@id="18"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_18(self):
        driver = self.app.driver
        self.m = 0
        for i in range(90, 95, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[18], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[18]
            item = driver.find_element_by_xpath('//*[@id="19"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_19(self):
        driver = self.app.driver
        self.m = 0
        for i in range(95, 100, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[19], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[19]
            item = driver.find_element_by_xpath('//*[@id="20"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_20(self):
        driver = self.app.driver
        self.m = 0
        for i in range(100, 105, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[20], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[20]
            item = driver.find_element_by_xpath('//*[@id="21"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_21(self):
        driver = self.app.driver
        self.m = 0
        for i in range(105, 110, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[21], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[21]
            item = driver.find_element_by_xpath('//*[@id="22"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_22(self):
        driver = self.app.driver
        self.m = 0
        for i in range(110, 115, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')              #Выводим весь массив
            # print(self.app.Schedule.massiv[22], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[22]
            item = driver.find_element_by_xpath('//*[@id="23"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def check_time_23(self):
        driver = self.app.driver
        self.m = 0
        for i in range(115, 120, 1):
            print(i, ' - инедекс, который подставляем в для поиска контейнера с архивом') #Выводим индекс, чтобы отследить ошибку list index out of range
            self.T = driver.find_elements_by_xpath(
                '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant" or @class="item empty "]')[
                i]
            # print(self.app.Schedule.massiv, ' массив из расписания')                               #Выводим весь массив
            # print(self.app.Schedule.massiv[23], ' элемент из массива, который мы берем')           #Выводим элемент из массива с нужным индексом
            self.item_time = self.app.Schedule.massiv[23]
            item = driver.find_element_by_xpath('//*[@id="24"]/td[1]')
            self.time_name = item.get_attribute('textContent')
            self.d = self.time_name.partition(':')[0]  # Получаем первую часть времени
            self.getting_time()
            self.check_for_emptiness()

    def getting_time(self):
        if self.m == 0:
            self.h1 = str(self.d) + ':' + str(self.m) + str('0')
            self.m = self.m + 12
            self.h2 = str(self.d) + ':' + str(self.m)
            self.h = self.h1 + '-' + self.h2
        else:
            self.h1 = str(self.d) + ':' + str(self.m)
            if self.m == 48:
                self.m = self.m + 11
                self.h2 = str(self.d) + ':' + str(self.m)
                self.h = self.h1 + '-' + self.h2
            else:
                self.h1 = str(self.d) + ':' + str(self.m)
                self.m = self.m + 12
                self.h2 = str(self.d) + ':' + str(self.m)
                self.h = self.h1 + '-' + self.h2

    def check_for_emptiness(self):
        if "item empty " in self.T.get_attribute('class'):
            item = 0
            if item == self.item_time:
                self.app.Messages_for_the_report.there_is_no_scheduled_archive()
            else:
                self.app.Messages_for_the_report.no_archive()
        else:
            self.T.click()
            self.app.Monitoring.check_player()


