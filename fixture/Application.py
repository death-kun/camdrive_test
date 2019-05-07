from selenium import webdriver
import time
from fixture.Authorization import AuthorizationHelper
from fixture.OnlinePageTestSuite import onlineTestSuite
from fixture.Localization_RU import Local_RU
from fixture.Player import player_check
from fixture.Archive import archive_check
from fixture.TopEditButtons import top_edit_buttons
from fixture.BottomEditButtons import bottom_edit_buttons


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('D:\python test\camdrive_test\chromedriver.exe')
        driver = self.driver
        driver.delete_all_cookies()
        self.Authorization = AuthorizationHelper(self)
        self.OnlinePageTestSuite = onlineTestSuite(self)
        self.Localization_RU = Local_RU(self)
        self.Player = player_check(self)
        self.Archive = archive_check(self)
        self.TopEditButtons = top_edit_buttons(self)
        self.BottomEditButtons = bottom_edit_buttons(self)


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



    def destroy(self):
        self.driver.quit()
