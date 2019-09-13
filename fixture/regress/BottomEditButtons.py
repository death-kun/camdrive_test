import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



class BottomEditButtons:

    def __init__(self, app):
        self.app = app

    def add_group(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        self.group_creation()
        #Проверка, что добавлеена Новая группа
        try:
            driver.find_element_by_xpath('//*[@id="node_4191"]/a')
            print('Проверка, что добавлеена новая группа. Проверка прошла успешно. Добавлена Новая группа')
            self.app.Authorization.logout_butten()
        except NoSuchElementException:
            print('Проверка, что добавлеена новая группа. Проверка провалилась. Новая группа не добавлена')
            self.app.Authorization.logout_butten()

    def group_creation(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_3063"]/a').click()
        driver.find_element_by_xpath('//*[@id="create-group"]').click()

    def rename_group(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        self.group_creation()
        driver.find_element_by_xpath('//*[contains(@title,"Новая группа")]').click()
        driver.find_element_by_css_selector('a.jstree-clicked')
        default_name_group = driver.find_element_by_css_selector('a.jstree-clicked').text
        driver.find_element_by_xpath('//*[@id="rename-group"]').click()
        time.sleep(1)
        name_group = driver.find_element_by_css_selector('input.jstree-rename-input')
        name_group.send_keys('test_name_group')
        name_group.send_keys(Keys.ENTER)
        time.sleep(1)
        new_name_group = driver.find_element_by_css_selector('a.jstree-clicked').text
        #Проверка, что изменилось имя Группы
        if new_name_group != default_name_group:
            print('Проверка, что изменилось имя группы. Проверка прошла успешно. Группа переименована')
            driver.find_element_by_xpath('//*[@id="remove-group"]').click()
            self.app.Authorization.logout_butten()
        else:
            print('Проверка, что изменилось имя группы. Проверка провалилась. Группа не переименована')
            self.app.Authorization.logout_butten()

    def group_deletion(self):
        driver = self.app.driver
        self.app.open_home_page()
        self.app.login_autotest()
        self.group_creation()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="remove-group"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[contains(@title,"Новая группа")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="remove-group"]').click()
        time.sleep(1)
        #Проверка, что Новая группа удалена
        try:
            driver.find_element_by_xpath('//*[contains(@title,"Новая группа")]')
            print('Проверка, что Новая группа удалена. Проверка провалилась. Новая группа не удалена.')
        except NoSuchElementException:
            print('Проверка, что Новая группа удалена. Проверка прошла успешно. Новая группа удалилась.')

