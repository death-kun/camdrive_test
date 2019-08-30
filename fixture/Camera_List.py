from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#TODO :: Добавить проверки на раскрыты группы или нет.

class cameralist:

    def __init__(self, app):
        self.app = app

    def click_camera_CD120_D521(self):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_4184']/a")))
        chanel = driver.find_element_by_xpath('//*[@id="node_4184"]')
        self.chanel_id = chanel.get_attribute('idi') #Получаем chanel_id камеры
        print(self.chanel_id)
        self.click_CD120_D521 = driver.find_element_by_xpath('//*[@id="node_4184"]/a').click()
        self.app.Monitoring.camera_title()

    def click_camera_CD_120(self):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_4343']/a")))
        chanel = driver.find_element_by_xpath('//*[@id="node_4343"]')
        self.chanel_id = chanel.get_attribute('idi')  # Получаем chanel_id камеры
        print(self.chanel_id)
        self.click_CD_120 = driver.find_element_by_xpath('//*[@id="node_4343"]/a').click()
        self.app.Monitoring.camera_title()

    def click_camera_CD100_E75A_ms3_dev(self):
        driver = self.app.driver
        try:
            self.app.Tree.second_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12605"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_12597']/a")))
        self.click_CD100_E75A_ms3_dev = driver.find_element_by_xpath('//*[@id="node_12597"]/a').click()  # камера CD100(E75A)_ms3_dev
        self.app.Monitoring.camera_title()

    def click_camera_CD100_E772_ms4(self):
        driver = self.app.driver
        try:
            self.app.Tree.second_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12605"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_6830']/a")))
        self.click_CD100_E772_ms4 = driver.find_element_by_xpath('//*[@id="node_6830"]/a').click()  # камера CD100(E772)_ms4_ПЗ
        self.app.Monitoring.camera_title()

    def click_camera_CD100_E778_ms5(self):
        driver = self.app.driver
        try:
            self.app.Tree.second_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12605"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_6827']/a")))
        self.click_CD100_E778_ms5 = driver.find_element_by_xpath('//*[@id="node_6827"]/a').click() # камера CD100(E778)_ms5_ПЗ
        self.app.Monitoring.camera_title()

    def click_camera_CD310_2E51_ms4_dev(self):
        driver = self.app.driver
        try:
            self.app.Tree.first_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12604"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_13959']/a")))
        self.click_CD310_2E51_ms4_dev = driver.find_element_by_xpath('//*[@id="node_13959"]/a').click()  # камера CD310(2E51)_ms4_dev
        self.app.Monitoring.camera_title()

    def click_CD320_AA06_ms3_dev(self):
        driver = self.app.driver
        try:
            self.app.Tree.first_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12604"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_12603']/a")))
        self.click_CD320_AA06_ms3_dev = driver.find_element_by_xpath('//*[@id="node_12603"]/a').click()  # камера CD320(AA06)_ms3_dev
        self.app.Monitoring.camera_title()

    def click_camera_CD320_AA78_ms5(self):
        driver = self.app.driver
        try:
            self.app.Tree.first_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12604"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_11460']/a")))
        self.click_CD320_AA78_ms5 = driver.find_element_by_xpath('//*[@id="node_11460"]/a').click()  # камера CD320(AA78)_ms5_Пр_С
        self.app.Monitoring.camera_title()

    def click_CD600_EF78_ms6_serv(self):
        driver = self.app.driver
        try:
            self.app.Tree.second_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12605"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_12601']/a")))
        self.click_CD600_EF78_ms6_serv = driver.find_element_by_xpath('//*[@id="node_12601"]/a').click()  # камера CD600(EF78)_ms6_serv
        self.app.Monitoring.camera_title()

    def click_camera_CD630_910D_ms6_dev(self):
        driver = self.app.driver
        try:
            self.app.Tree.first_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12604"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_12602']/a")))
        self.click_CD630_910D_ms6_dev = driver.find_element_by_xpath('//*[@id="node_12602"]/a').click()  # камера CD630(910D)_ms6_dev
        self.app.Monitoring.camera_title()

    def click_camera_N1001_3A00_bwd(self):
        driver = self.app.driver
        try:
            self.app.Tree.second_tree()
        except:
            driver.find_element_by_xpath('//*[@id="node_12605"]/ins').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='node_14875']/a")))
        self.click_N1001_3A00_bwd = driver.find_element_by_xpath('//*[@id="node_14875"]/a').click()  # камера N1001(3A00)_bwd
        self.app.Monitoring.camera_title()