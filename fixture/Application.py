from selenium import webdriver



class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('D:\python test\camdrive\chromedriver.exe')
        driver = self.driver
        driver.delete_all_cookies()

    def Authorization(self):
        driver = self.driver
        driver.get('http://test.camdrive.org/')
        login = driver.find_element_by_xpath('//*[@id="login-box"]/form/table/tbody/tr[1]/td[2]/input')
        login.send_keys('autotest')
        password = driver.find_element_by_xpath('//*[@id="login-box"]/form/table/tbody/tr[2]/td[2]/div/input[1]')
        password.send_keys('autotest')




    def Stop(self):
        self.driver.quit()
