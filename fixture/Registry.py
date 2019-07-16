import winreg

class regedit:

    def __init__(self, app):
        self.app = app

    def check_registry(self):
        reg_path = 'Software\Policies\Google\Chrome\PluginsAllowedForUrls' #Путь
        url = "https://test.camdrive.org" #Сайт, на котором должен быть включен flash
        VALUE_NAME = "1" #Название параметра

        try:
            KEY_READ = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
            print(
                'Указанный раздел существует')
            try:
                value, regtype = winreg.QueryValueEx(KEY_READ, VALUE_NAME)
                print('Есть такой параметр')
            except FileNotFoundError:
                print('Нет такого строкового параметра')

                try:
                    KEY_WRITE = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
                    winreg.SetValueEx(KEY_WRITE, VALUE_NAME, 0, winreg.REG_SZ, url)
                    winreg.CloseKey(KEY_WRITE)
                    print('Создан строковый параметр')
                except:
                    print('Не создан строковый параметр')

        except EnvironmentError:
            print('Указанный раздел не существует')
