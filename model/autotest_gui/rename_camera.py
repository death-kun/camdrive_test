class rename:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        driver = self.app.driver
        self.app.Authorization.open_home_page()
        self.app.Authorization.login_autotest()
        old_name_camera = driver.find_element_by_xpath('//*[@id="node_4184"]/a').text
        self.app.TopEditButtons.camera_rename_button()
        new_name_camera = driver.find_element_by_xpath('//*[@id="node_4184"]/a').text
        # Проверка, что изменилось имя камеры
        if new_name_camera != old_name_camera:
            print('Проверка, что изменилось имя камеры. Проверка прошла успешно. Камера переименована')
            if 'test_name' in new_name_camera:
                self.app.TopEditButtons.camera_rename_CD120_D521()
        else:
            print('Проверка, что изменилось имя камеры. Проверка провалилась. Камера не переименована')
            self.app.Authorization.logout_butten()
