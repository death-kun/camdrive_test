
class balance_LK:

    def __init__(self, app):
        self.app = app

    def autotest_balance(self):
        self.app.Monitoring.delete_txt()
        self.app.Balance.request_balance()
        self.app.login_autotest()
        self.app.Balance.balance_gui()
        self.app.Monitoring.find_yesterday()
        if self.app.Balance.parsing_balance_attribute == self.app.Balance.parsing3:
            print('Проверка баланса прошла успешно. Баланс запросом совпадает с балансом, который отображается в ЛК')
            with open('check balance report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"' + self.app.Monitoring.strg_today + '" "Проверка баланса" INFO: Проверка выполнена. Баланс = '+ self.app.Balance.parsing_balance_attribute +' р.\n')
                f.close()
        else:
            print('Проверка баланса провалилась. Баланс запросом не совпадает с балансом, который отображается в ЛК')
            with open('check balance errore report.txt', 'a', encoding='utf-8') as f:
                f.write(
                    '"' + self.app.Monitoring.strg_today + '" "Проверка баланса" WARNING: Проверка пропалилась. Баланс отображающийся в ЛК не совпадает с балансом, который отправляет серве.\n')
                f.close()
        self.app.logout_butten()