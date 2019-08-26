from selenium import webdriver
import time
from sys import platform
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
from fixture.monitoring.Date_determination import DateDetermination
from fixture.monitoring.Messages_for_the_report import messages
#общее
from fixture.Camera_List import cameralist
from fixture.Requests import requests_camdrive
from fixture.Tree import camera_tree
from fixture.Registry import regedit
from fixture.RMS import rms
#тесты
from model.autotest_gui.download_archive import downloadarchive
from model.autotest_gui.balance_check import balance_LK
from model.autotest_gui.rename_camera import rename
from model.autotest_gui.enter_with_invalid_login import invalid_login
from model.autotest_gui.enter_with_invalid_password import invalid_password
from model.autotest_gui.password_visibility_check import password_visibility
from model.autotest_gui.login_check_with_valid_data import valid_data
from model.autotest_gui.check_activity_checkbox import checkbox
from model.autotest_gui.check_forgot_your_password_gui import forgot_your_password
#тестовые камеры
from model.monitoring_archive.camera_CD120_D521 import CD120_D521
from model.monitoring_archive.camera_CD_120 import CD_120
from model.monitoring_online.CD120_D521 import CD120_D521_online
from model.monitoring_online.CD_120 import CD_120_online
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
        self.Camera_List = cameralist(self)
        self.download_archive = downloadarchive(self)
        self.Balance = balance(self)
        self.balance_check = balance_LK(self)
        self.Online = checkonlune(self)
        self.rename_camera = rename(self)
        self.Requests = requests_camdrive(self)
        self.enter_with_invalid_login = invalid_login(self)
        self.enter_with_invalid_password = invalid_password(self)
        self.password_visibility_check = password_visibility(self)
        self.login_check_with_valid_data = valid_data(self)
        self.check_activity_checkbox = checkbox(self)
        self.check_forgot_your_password_gui = forgot_your_password(self)
        self.Tree = camera_tree(self)
        self.Registry = regedit(self)
        self.Date_determination = DateDetermination(self)
        self.RMS = rms(self)
        self.Messages_for_the_report = messages(self)

        #тестовые камеры
        self.camera_CD120_D521 = CD120_D521(self)
        self.camera_CD_120 = CD_120(self)
        self.CD120_D521 = CD120_D521_online(self)
        self.CD_120 = CD_120_online(self)

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

    def destroy(self):
        self.driver.quit()
