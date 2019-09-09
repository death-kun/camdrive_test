from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CameraTree:

    def __init__(self, app):
        self.app = app

    def first_tree(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_12602"]/a')
        driver.find_element_by_xpath('//*[@id="node_12603"]/a')
        driver.find_element_by_xpath('//*[@id="node_11460"]/a')
        driver.find_element_by_xpath('//*[@id="node_13959"]/a')

    def second_tree(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="node_6830"]/a')
        driver.find_element_by_xpath('//*[@id="node_14875"]/a')
        driver.find_element_by_xpath('//*[@id="node_12601"]/a')
        driver.find_element_by_xpath('//*[@id="node_6827"]/a')
        driver.find_element_by_xpath('//*[@id="node_12597"]/a')

    def testing_group2(self):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="node_4184"]/a')))
        driver.find_element_by_xpath('//*[@id="node_4184"]/a')

    def testing_group(self):
        driver = self.app.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="node_4343"]/a')))
        driver.find_element_by_xpath('//*[@id="node_4343"]/a')