from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class cameralist:

    def __init__(self, app):
        self.app = app

    def click_camera_CD120_D521(self):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_4184']/a")))
        self.click_CD120_D521 = driver.find_element_by_xpath('//*[@id="node_4184"]/a').click()
        self.app.Monitoring.camera_title()

    def click_camera_CD_120(self):
        driver = self.app.driver
        self.click_CD_120 = driver.find_element_by_xpath('//*[@id="node_4343"]/a')
        self.click_CD_120.click()
        self.app.Monitoring.camera_title()

    def click_camera_CD100_E75A_ms3_dev(self):
        driver = self.app.driver
        self.click_CD100_E75A_ms3_dev = driver.find_element_by_xpath('//*[@id="node_12597"]/a')  # камера CD100(E75A)_ms3_dev
        self.click_CD100_E75A_ms3_dev.click()
        self.app.Monitoring.camera_title()

    def click_camera_CD100_E772_ms4(self):
        driver = self.app.driver
        self.click_CD100_E772_ms4 = driver.find_element_by_xpath('//*[@id="node_6830"]/a')  # камера CD100(E772)_ms4_ПЗ
        self.click_CD100_E772_ms4.click()
        self.app.Monitoring.camera_title()

    def click_camera_CD100_E778_ms5(self):
        driver = self.app.driver
        self.click_CD100_E778_ms5 = driver.find_element_by_xpath('//*[@id="node_6827"]/a')  # камера CD100(E778)_ms5_ПЗ
        self.click_CD100_E778_ms5.click()
        self.app.Monitoring.camera_title()

    def click_camera_CD310_2E51_ms4_dev(self):
        driver = self.app.driver
        self.click_CD310_2E51_ms4_dev = driver.find_element_by_xpath('//*[@id="node_13959"]/a')  # камера CD310(2E51)_ms4_dev
        self.click_CD310_2E51_ms4_dev.click()
        self.app.Monitoring.camera_title()

    def click_CD320_AA06_ms3_dev(self):
        driver = self.app.driver
        self.click_CD320_AA06_ms3_dev = driver.find_element_by_xpath('//*[@id="node_12603"]/a')  # камера CD320(AA06)_ms3_dev
        self.click_CD320_AA06_ms3_dev.click()
        self.app.Monitoring.camera_title()

    def click_camera_CD320_AA78_ms5(self):
        driver = self.app.driver
        self.click_CD320_AA78_ms5 = driver.find_element_by_xpath('//*[@id="node_11460"]/a')  # камера CD320(AA78)_ms5_Пр_С
        self.click_CD320_AA78_ms5.click()
        self.app.Monitoring.camera_title()

    def click_CD600_EF78_ms6_serv(self):
        driver = self.app.driver
        self.click_CD600_EF78_ms6_serv = driver.find_element_by_xpath('//*[@id="node_12601"]/a')  # камера CD600(EF78)_ms6_serv
        self.click_CD600_EF78_ms6_serv.click()
        self.app.Monitoring.camera_title()

    def click_camera_CD630_910D_ms6_dev(self):
        driver = self.app.driver
        self.click_CD630_910D_ms6_dev = driver.find_element_by_xpath('//*[@id="node_12602"]/a')  # камера CD630(910D)_ms6_dev
        self.click_CD630_910D_ms6_dev.click()
        self.app.Monitoring.camera_title()

    def click_camera_N1001_3A00_bwd(self):
        driver = self.app.driver
        self.click_N1001_3A00_bwd = driver.find_element_by_xpath('//*[@id="node_14875"]/a')  # камера N1001(3A00)_bwd
        self.click_N1001_3A00_bwd.click()
        self.app.Monitoring.camera_title()