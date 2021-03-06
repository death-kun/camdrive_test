import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

class Schedule:

    def __init__(self, app):
        self.app = app

#TODO :: Придумать корректную проверку на раскрыто дерево или нет
    def open_schedule(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="navigation"]/table/tbody/tr/td[3]/a').click()
        driver.find_element_by_xpath('//*[@id="subsections"]/table/tbody/tr/td[2]/a').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'jstree-open')))
        self.camera_name_shedule = self.app.Monitoring.camera_name
        self.app.Monitoring.title_camera()
        if self.app.Monitoring.camera_name == self.camera_name_shedule:
            return True
        else:
            self.app.DateDetermination.find_yesterday()
            self.app.MessagesForTheReport.wrong_camera_selected()
            url = driver.current_url
            if url != 'https://test.camdrive.org/settings/schedule':
                self.app.Tree.check_second_tree()
                self.app.Tree.check_first_tree()
            else:
                self.app.Tree.check_testing_gruop()
                self.app.Tree.check_testing_gruop2()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#" and contains(text(), "' + self.camera_name_shedule.strip() + '")]')))
            driver.find_element_by_xpath('//a[@href="#" and contains(text(), "' + self.camera_name_shedule.strip() + '")]').click()

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
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="schedule"]/table[1]/tbody/tr[7]/td[' + str(td) + ']')))
            self.schedule_cell = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[7]/td[' + str(td) + ']')
            self.array_of_schedule_cells()

    def saturday(self):
        driver = self.app.driver
        # Суббота
        self.massiv = []
        for td in range(2, 26, 1):
            self.schedule_cell = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[6]/td[' + str(td) + ']')
            self.array_of_schedule_cells()

    def friday(self):
        driver = self.app.driver
        # Пятница
        self.massiv = []
        for td in range(2, 26, 1):
            self.schedule_cell = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[5]/td[' + str(td) + ']')
            self.array_of_schedule_cells()

    def thursday(self):
        driver = self.app.driver
        # Четверг
        self.massiv = []
        for td in range(2, 26, 1):
            self.schedule_cell = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[4]/td[' + str(td) + ']')
            self.array_of_schedule_cells()

    def wednesday(self):
        driver = self.app.driver
        # Среда
        self.massiv = []
        for td in range(2, 26, 1):
            self.schedule_cell = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[3]/td[' + str(td) + ']')
            self.array_of_schedule_cells()

    def tuesday(self):
        driver = self.app.driver
        # Вторник
        self.massiv = []
        for td in range(2, 26, 1):
            self.schedule_cell = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[2]/td[' + str(td) + ']')
            self.array_of_schedule_cells()

    def monday(self):
        driver = self.app.driver
        # Понедельник
        self.massiv = []
        for td in range(2, 26, 1):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="schedule"]/table[1]/tbody/tr[1]/td[' + str(td) + ']')))
            self.schedule_cell = driver.find_element_by_xpath('//*[@id="schedule"]/table[1]/tbody/tr[1]/td[' + str(td) + ']')
            self.array_of_schedule_cells()

    def array_of_schedule_cells(self):
        if self.massiv == []:
            self.check_attribute()
            self.massiv = [self.element_time]
        else:
            self.check_attribute()
            self.massiv.append(self.element_time)
        # print(self.massiv)

    def check_attribute(self):
        attempt = 0
        while attempt < 2:
            try:
                if "item detection" in self.schedule_cell.get_attribute("class"):
                    self.element_time = 2  # 2 = запись по детекции
                elif "item constant" in self.schedule_cell.get_attribute("class"):
                    self.element_time = 1  # 1 = запись есть
                else:
                    self.element_time = 0  # 0 = нет записи
                break
            except StaleElementReferenceException:
                self.app.MessagesForTheReport.error_StaleElementReferenceException()
                attempt +=1