from selenium import webdriver
import time
from sys import platform
from fixture.regress.Authorization import AuthorizationHelper
from fixture.regress.OnlinePageTestSuite import onlineTestSuite
from fixture.regress.Localization_RU import Local_RU
from fixture.regress.Player import player_check
from fixture.regress.Archive import archive_check
from fixture.regress.TopEditButtons import top_edit_buttons
from fixture.regress.BottomEditButtons import bottom_edit_buttons
from fixture.monitoring.Monitoring import monitoring
from fixture.monitoring.Schedule import schedule
from fixture.monitoring.LineHours import hours
from model.camera_CD120_D521 import CD120_D521
from model.camera_CD_120 import CD_120

class Application:

    def __init__(self):
        if platform == "linux" or platform == "linux2":
            self.driver = webdriver.Chrome('/home/mikhail/PycharmProjects/camdrive_test/chromedriver')  # для ubuntu
        elif platform == "win32":
            self.driver = webdriver.Chrome()  # для windows
        driver = self.driver
        driver.delete_all_cookies()

        self.Authorization = AuthorizationHelper(self)
        self.OnlinePageTestSuite = onlineTestSuite(self)
        self.Localization_RU = Local_RU(self)
        self.Player = player_check(self)
        self.Archive = archive_check(self)
        self.TopEditButtons = top_edit_buttons(self)
        self.BottomEditButtons = bottom_edit_buttons(self)
        self.Monitoring = monitoring(self)
        self.Schedule = schedule(self)
        self.LineHours = hours(self)
        self.camera_CD120_D521 = CD120_D521(self)
        self.camera_CD_120 = CD_120(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        driver.get('http://test.camdrive.org/')

    def login_autotest(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_xpath('//input[@name="username"]').send_keys('autotest')
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('autotest')
        driver.find_element_by_id('login').click()
        time.sleep(1)

    def logout_butten(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[1]/td[2]/input').click()

    def forgot_your_password(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_link_text('Забыли пароль?').click()
        #Проверка перехода на форму "Забыли пароль?"
        if driver.find_element_by_css_selector('.info-title').text == "Восстановление пароля":
            print('Проверка перехода на форму "Забыли пароль?". Проверка прошла успешно. Открылась форма "Забыли пароль?".')
        else:
            print('Проверка перехода на форму "Забыли пароль?". Проверка провалилась. Форма "Забыли пароль?" не открылась.')

    def tick_activity(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_xpath('/html/body/div/div/form/table/tbody/tr[3]/td[2]/input[2]').click()
        time.sleep(1)
        isChecked = driver.find_element_by_xpath('/html/body/div/div/form/table/tbody/tr[3]/td[2]/input[2]').get_attribute("checked")
        #Проверка активности "галочки"
        if isChecked is not None:
            print('Проверка авктивности "галочки". Проверка прошла успешно. Галочка поставилась в чекбокс')
        else:
            print('Проверка авктивности "галочки". Проверка провалилась. Галочка не поставилась в чекбокс')

    def open_archive(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/a').click()
        driver.find_element_by_css_selector('div.item.day.today').click()
        time.sleep(1)
        click_element = driver.find_element_by_xpath(
            '//div[@id="time-intervals"]//td//div[@class="time item  button" or @class="time item  detection" or @class="time item  constant"]')
        time.sleep(1)
        click_element.click()
        time.sleep(2)

    def first_tree(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="node_12602"]/a')
        driver.find_element_by_xpath('//*[@id="node_12603"]/a')
        driver.find_element_by_xpath('//*[@id="node_11460"]/a')
        driver.find_element_by_xpath('//*[@id="node_13959"]/a')


    def second_tree(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="node_6830"]/a')
        driver.find_element_by_xpath('//*[@id="node_14875"]/a')
        driver.find_element_by_xpath('//*[@id="node_12601"]/a')
        driver.find_element_by_xpath('//*[@id="node_6827"]/a')
        driver.find_element_by_xpath('//*[@id="node_12597"]/a')

    def destroy(self):
        self.driver.quit()
