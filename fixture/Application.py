from selenium import webdriver
import time
from sys import platform
#для регреса
from fixture.regress.Authorization import AuthorizationHelper
from fixture.regress.OnlinePageTestSuite import onlineTestSuite
from fixture.regress.Localization_RU import LocalRU
from fixture.regress.Player import PlayerCheck
from fixture.regress.Archive import ArchiveCheck
from fixture.regress.TopEditButtons import TopEditButtons
from fixture.regress.BottomEditButtons import BottomEditButtons
from fixture.regress.Balance import Balance
#для мониторинга
from fixture.monitoring.Monitoring import Monitoring
from fixture.monitoring.Schedule import Schedule
from fixture.monitoring.LineHours import Hours
from fixture.monitoring.Online import CheckOnlune
from fixture.monitoring.Date_determination import DateDetermination
from fixture.monitoring.Messages_for_the_report import Messages
#общее
from fixture.Camera_List import CameraList
from fixture.Requests import RequestsCamdrive
from fixture.Tree import CameraTree
from fixture.Registry import Regedit
from fixture.RMS import RMS
from fixture.Delete_TXT_files import DeleteTxtFile
#тесты
from model.autotest_gui.download_archive import DownloadArchive
from model.autotest_gui.balance_check import BalanceLK
from model.autotest_gui.check_top_edit_buttons import CheckTopEditButtons
from model.autotest_gui.enter_with_invalid_login import InvalidLogin
from model.autotest_gui.enter_with_invalid_password import InvalidPassword
from model.autotest_gui.password_visibility_check import PasswordVisibility
from model.autotest_gui.login_check_with_valid_data import ValidData
from model.autotest_gui.check_activity_checkbox import Checkbox
from model.autotest_gui.check_forgot_your_password_gui import ForgotYourPassword
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

        self.Authorization = AuthorizationHelper(self)
        self.OnlinePageTestSuite = onlineTestSuite(self)
        self.Localization_RU = LocalRU(self)
        self.Player = PlayerCheck(self)
        self.Archive = ArchiveCheck(self)
        self.TopEditButtons = TopEditButtons(self)
        self.BottomEditButtons = BottomEditButtons(self)
        self.Monitoring = Monitoring(self)
        self.Schedule = Schedule(self)
        self.LineHours = Hours(self)
        self.CameraList = CameraList(self)
        self.DownloadArchive = DownloadArchive(self)
        self.Balance = Balance(self)
        self.BalanceCheck = BalanceLK(self)
        self.Online = CheckOnlune(self)
        self.CheckTopEditButtons = CheckTopEditButtons(self)
        self.Requests = RequestsCamdrive(self)
        self.EnterWithInvalidLogin = InvalidLogin(self)
        self.EnterWithInvalidPassword = InvalidPassword(self)
        self.PasswordVisibilityCheck = PasswordVisibility(self)
        self.LoginCheckWithValidData = ValidData(self)
        self.CheckActivityCheckbox = Checkbox(self)
        self.CheckForgotYourPasswordGui = ForgotYourPassword(self)
        self.Tree = CameraTree(self)
        self.Registry = Regedit(self)
        self.DateDetermination = DateDetermination(self)
        self.RMS = RMS(self)
        self.MessagesForTheReport = Messages(self)
        self.DeleteTxtFiles = DeleteTxtFile(self)

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
