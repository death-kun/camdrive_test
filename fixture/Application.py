from selenium import webdriver



class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('D:\python test\camdrive_test\chromedriver.exe')
        driver = self.driver
        driver.delete_all_cookies()

    def Authorization(self):
        driver = self.driver
        driver.get('http://test.camdrive.org/')
        login = driver.find_element_by_xpath('//input[@name="username"]')
        login.send_keys('autotest')
        password = driver.find_element_by_xpath('//input[@name="password"]')
        password.send_keys('111')




    def Stop(self):
        self.driver.quit()
