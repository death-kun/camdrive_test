import sys
import ctypes
import winreg

class regedit:

    def __init__(self, app):
        self.app = app

    # Метод check_registry делает проверку на наличие Раздела PluginsAllowedForUrls и параметра 1.
    # Если нет параметра, то он создается.
    # Для выполнения данной проверки необходимо запускать от администратора.

    # def check_registry(self):
    #
    #
    #     reg_path = r'Software\Policies\Google\Chrome\PluginsAllowedForUrls' #Путь
    #     url = "https://test.camdrive.org" #Сайт, на котором должен быть включен flash
    #     VALUE_NAME = "1" #Название параметра
    #
    #     try:
    #         KEY_READ = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
    #         print('Указанный раздел существует')
    #
    #         try:
    #             value, regtype = winreg.QueryValueEx(KEY_READ, VALUE_NAME)
    #             print('Есть такой параметр')
    #             winreg.CloseKey(KEY_READ)
    #         except FileNotFoundError:
    #             print('Нет такого строкового параметра')
    #
    #             try:
    #                 KEY_WRITE = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
    #                 winreg.SetValueEx(KEY_WRITE, VALUE_NAME, 0, winreg.REG_SZ, url)
    #                 winreg.CloseKey(KEY_WRITE)
    #                         # winreg.CloseKey(KEY_READ)
    #                 print('Создан строковый параметр')
    #             except:
    #                 print('Не создан строковый параметр')
    #
    #     except EnvironmentError:
    #         print('Указанный раздел не существует')



    # def is_admin(self):
    #     try:
    #         return ctypes.windll.shell32.IsUserAnAdmin()
    #     except:
    #         return False
    #
    # def execute(self):
    #     if self.is_admin():
    #         reg_path = r'Software\Policies\Google\Chrome\PluginsAllowedForUrls'  # Путь
    #         url = "https://test.camdrive.org"  # Сайт, на котором должен быть включен flash
    #         VALUE_NAME = "1"  # Название параметра
    #
    #         try:
    #             KEY_READ = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
    #             print('Указанный раздел существует')
    #
    #             try:
    #                 value, regtype = winreg.QueryValueEx(KEY_READ, VALUE_NAME)
    #                 print('Есть такой параметр')
    #                 winreg.CloseKey(KEY_READ)
    #             except FileNotFoundError:
    #                 print('Нет такого строкового параметра')
    #
    #                 try:
    #                     KEY_WRITE = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
    #                     winreg.SetValueEx(KEY_WRITE, VALUE_NAME, 0, winreg.REG_SZ, url)
    #                     winreg.CloseKey(KEY_WRITE)
    #                     # winreg.CloseKey(KEY_READ)
    #                     print('Создан строковый параметр')
    #                 except:
    #                     print('Не создан строковый параметр')
    #
    #         except EnvironmentError:
    #             print('Указанный раздел не существует')
    #     else:
    #         # Re-run the program with admin rights
    #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    #         print('HZ Cho')