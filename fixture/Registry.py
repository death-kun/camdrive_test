from winreg import *
import sys

class regedit:

    def __init__(self, app):
        self.app = app

    def check_registry(self):
        reg_path = 'Software\Policies\Google\Chrome\PluginsAllowedForUrls'
        allow_flash = {'1': 'https://test.camdrive.org'}

        if sys.platform == 'win32':
            try:
                try:
                    RegistryKey = OpenKey(HKEY_CURRENT_USER, reg_path, 0, KEY_ALL_ACCESS)
                    for K, V in allow_flash.items():
                        try:
                            if QueryValueEx(RegistryKey, K)[0] == V:
                                pass
                            else:
                                SetValueEx(RegistryKey, K, 0, REG_SZ, V)
                        except FileNotFoundError:
                            SetValueEx(RegistryKey, K, 0, REG_SZ, V)
                    CloseKey(RegistryKey)
                except FileNotFoundError:
                    RegistryKey = CreateKey(HKEY_CURRENT_USER, reg_path)
                    for K, V in allow_flash.items():
                        SetValueEx(RegistryKey, K, 0, REG_SZ, V)
                    CloseKey(RegistryKey)
            except:
                pass