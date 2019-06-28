import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class schedule:

    def __init__(self, app):
        self.app = app

    def open_schedule(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="navigation"]/table/tbody/tr/td[3]/a').click()
        driver.find_element_by_xpath('//*[@id="subsections"]/table/tbody/tr/td[2]/a').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li#node_3063.jstree-last.jstree-open')))
        self.camera_name_shedule = self.app.Monitoring.title()
        if self.app.Monitoring.camera_name == self.camera_name_shedule:
            return True
        else:
            driver.find_element_by_xpath('//*contains(text(), "' + str(self.app.Monitoring.camera_name) + '")')
            self.app.click_camera.click()

    def schedule_first_tree(self):
        self.app.check_first_tree()

    def schedule_second_tree(self):
        self.app.check_second_tree()

    def yesterday_day_of_the_week(self):
        now = datetime.datetime.today().weekday()
        if now > 0:
            yesterday_weekday = now - 1
        else:
            yesterday_weekday = now + 6

        #Циферное обозначение дней недели
        Mon = 0
        W = 1
        Wed = 2
        Th = 3
        Fri = 4
        Sat = 5
        Sun = 6

        if yesterday_weekday == Mon:
            self.monday()
        elif yesterday_weekday == W:
            self.tuesday()
        elif yesterday_weekday == Wed:
            self.wednesday()
        elif yesterday_weekday == Th:
            self.thursday()
        elif yesterday_weekday == Fri:
            self.friday()
        elif yesterday_weekday == Sat:
            self.saturday()
        elif yesterday_weekday == Sun:
            self.sunday()

    def sunday(self):
        driver = self.app.driver
        # Воскресенье
        self.massiv = []
        for td in range(2, 26, 1):
            self.time = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[' + str(td) + ']')
            self.elem_time()

    def saturday(self):
        driver = self.app.driver
        # Суббота
        self.massiv = []
        for td in range(2, 26, 1):
            self.time = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[' + str(td) + ']')
            self.elem_time()

    def friday(self):
        driver = self.app.driver
        # Пятница
        self.massiv = []
        for td in range(2, 26, 1):
            self.time = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[' + str(td) + ']')
            self.elem_time()

    def thursday(self):
        driver = self.app.driver
        # Четверг
        self.massiv = []
        for td in range(2, 26, 1):
            self.time = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[' + str(td) + ']')
            self.elem_time()

    def wednesday(self):
        driver = self.app.driver
        self.massiv = []
        for td in range(2, 26, 1):
            self.time = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[' + str(td) + ']')
            self.elem_time()
            print(td)

    def tuesday(self):
        driver = self.app.driver
        # Вторник
        self.time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[2]')
        self.massiv = []
        for td in range(2, 26, 1):
            self.time = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[' + str(td) + ']')
            self.elem_time()

    def monday(self):
        driver = self.app.driver
        # Понедельник
        self.time_0 = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[2]')
        self.massiv = []
        for td in range(2, 26, 1):
            self.time = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[' + str(td) + ']')
            self.elem_time()

    def elem_time(self):
        if self.massiv == 0:
            self.check_attribute()
            self.massiv = [self.element_time]
        else:
            self.check_attribute()
            self.massiv.append(self.element_time)

        print(self.massiv)

    def check_attribute(self):
        if "item " in self.time.get_attribute("class"):
            self.element_time = 0  # 0 = нет записи
        elif "item detection" in self.time.get_attribute("class"):
            self.element_time = 2  # 2 = запись по детекции
        else:
            self.element_time = 1  # 1 = запись есть