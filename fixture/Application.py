from selenium import webdriver
import time
from sys import platform
from selenium.webdriver.chrome.options import Options

#для регреса
from fixture.regress.Authorization import AuthorizationHelper
from fixture.regress.OnlinePageTestSuite import onlineTestSuite
from fixture.regress.Localization_RU import Local_RU
from fixture.regress.Player import player_check
from fixture.regress.Archive import archive_check
from fixture.regress.TopEditButtons import top_edit_buttons
from fixture.regress.BottomEditButtons import bottom_edit_buttons
from fixture.regress.Balance import balance
#для мониторинга
from fixture.monitoring.Monitoring import monitoring
from fixture.monitoring.Schedule import schedule
from fixture.monitoring.LineHours import hours
from fixture.monitoring.Online import checkonlune
#общее
from fixture.Camera_List import cameralist
#тесты
from model.autotest_gui.download_archive import downloadarchive
from model.autotest_gui.balance_check import balance_LK
#тестовые камеры
from model.monitoring_archive.camera_CD120_D521 import CD120_D521
from model.monitoring_archive.camera_CD_120 import CD_120
from model.monitoring_online.CD120_D521 import CD120_D521_online
#рабочие камеры
from model.monitoring_archive.camera_CD100_E75A_ms3_dev import CD100_E75A_ms3_dev
from model.monitoring_archive.camera_CD100_E778_ms5 import CD100_E778_ms5
from model.monitoring_archive.camera_CD600_EF78_ms6_serv import CD600_EF78_ms6_serv
from model.monitoring_archive.camera_CD630_910D_ms6_dev import CD630_910D_ms6_dev
from model.monitoring_archive.camera_CD320_AA06_ms3_dev import CD320_AA06_ms3_dev
from model.monitoring_archive.camera_CD320_AA78_ms5 import CD320_AA78_ms5
from model.monitoring_archive.camera_CD310_2E51_ms4_dev import CD310_2E51_ms4_dev
from model.monitoring_archive.camera_CD100_E772_ms4 import CD100_E772_ms4
from model.monitoring_archive.camera_N1001_3A00_bwd import N1001_3A00_bwd


class Application:

    def __init__(self):
        if platform == "linux" or platform == "linux2":
            self.driver = webdriver.Chrome('/home/mikhail/PycharmProjects/camdrive_test/chromedriver')  # для ubuntu
        elif platform == "win32":
            chrome_options = Options()
            chrome_options.add_argument("--disable-features=EnableEphemeralFlashPermission")

            extensions = {"profile.default_content_setting_values.plugins": 1,
                            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
                            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
                            "PluginsAllowedForUrls": "https://test.camdrive.org/online"}

            chrome_options.add_experimental_option("prefs", extensions)
            chrome_options.add_argument('--disable-features=EnableEphemeralFlashPermission')
            chrome_options.add_argument('--disable-infobars')
            chrome_options.add_argument("--ppapi-flash-version=32.0.0.207")

            self.driver = webdriver.Chrome(options=chrome_options)
            # self.driver = webdriver.Chrome()  # для windows
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
        self.Camera_List = cameralist(self)
        self.download_archive = downloadarchive(self)
        self.Balance = balance(self)
        self.balance_check = balance_LK(self)
        self.Online = checkonlune(self)
        #тестовые камеры
        self.camera_CD120_D521 = CD120_D521(self)
        self.camera_CD_120 = CD_120(self)
        self.CD120_D521 = CD120_D521_online(self)
        #рабочие камеры
        self.camera_CD100_E778_ms5 = CD100_E778_ms5(self)
        self.camera_CD100_E75A_ms3_dev = CD100_E75A_ms3_dev(self)
        self.camera_CD600_EF78_ms6_serv = CD600_EF78_ms6_serv(self)
        self.camera_CD630_910D_ms6_dev = CD630_910D_ms6_dev(self)
        self.camera_CD320_AA06_ms3_dev = CD320_AA06_ms3_dev(self)
        self.camera_CD320_AA78_ms5 = CD320_AA78_ms5(self)
        self.camera_CD310_2E51_ms4_dev = CD310_2E51_ms4_dev(self)
        self.camera_CD100_E772_ms4 = CD100_E772_ms4(self)
        self.camera_N1001_3A00_bwd = N1001_3A00_bwd(self)


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
