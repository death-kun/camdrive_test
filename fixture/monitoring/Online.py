import imgdiff
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class checkonlune:

    def __init__(self, app):
        self.app = app



    def online_screenshot(self):
        screenshot_error = imgdiff.Image.open("D:/python test/camdrive_test/test/1.png")
        driver = self.app.driver
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="flash_1"]')))
            i = 0
            p1 = 0
            while i < 10:
                driver.find_element_by_xpath('//*[@id="screens"]/div[1]/div/div[2]/div').screenshot("1.png")
                self.p = imgdiff.Image.open("D:/python test/camdrive_test/1.png")
                # time.sleep(1)
                if self.p == p1:
                    print('-онлайн не идет')
                    if imgdiff.ImageChops.darker(screenshot_error, self.p):
                        print('--отображается серверное сообщение')
                    else:
                        print('--не сообщение')
                else:
                    print('-онлайн идет')

                p1 = self.p
                i += 1
        except TimeoutException:
            print('не загрузился плеер')




