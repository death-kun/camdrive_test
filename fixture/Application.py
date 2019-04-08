from selenium import webdriver
import time
from fixture.Authorization import AuthorizationHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('D:\python test\camdrive_test\chromedriver.exe')
        driver = self.driver
        driver.delete_all_cookies()
        self.Authorization = AuthorizationHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get('http://test.camdrive.org/')

    def forgot_your_password(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[1]/td[2]/input').click()
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
        #Проверка авктивности "галочки"
        if isChecked is not None:
            print('Проверка авктивности "галочки". Проверка прошла успешно. Галочка поставилась в чекбокс')
        else:
            print('Проверка авктивности "галочки". Проверка провалилась. Галочка не поставилась в чекбокс')


    def Stop(self):
        self.driver.quit()
