import time

class Checkbox:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        driver = self.app.driver
        driver.find_element_by_xpath('/html/body/div/div/form/table/tbody/tr[3]/td[2]/input[2]').click()
        time.sleep(1)
        isChecked = driver.find_element_by_xpath('/html/body/div/div/form/table/tbody/tr[3]/td[2]/input[2]').get_attribute("checked")
        #Проверка активности "галочки"
        if isChecked is not None:
            print('Проверка авктивности "галочки". Проверка прошла успешно. Галочка поставилась в чекбокс')
        else:
            print('Проверка авктивности "галочки". Проверка провалилась. Галочка не поставилась в чекбокс')