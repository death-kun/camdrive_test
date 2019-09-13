
class Balance:

    def __init__(self, app):
        self.app = app

    def balance_gui(self):
        driver = self.app.driver
        pay_balance = driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td[1]/div/span')
        balance_attribute = pay_balance.get_attribute('textContent')
        self.parsing_balance_attribute = balance_attribute.replace('p', '')
        print(self.parsing_balance_attribute, 'Баланс, который отображается в ЛК')