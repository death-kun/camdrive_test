
# def test_Log_In(app):
#     app.Authorization.login_with_incorrect_data() #Проверка того, что указан не верный пароль
#     app.Authorization.password_visibility_check() #Проверка, что при нажатии на "глаз" видно введенный пароль
#     app.Authorization.login_with_valid_data() #Проверка того, что указан верный логин и пароль
#
# def test_Forgot_Your_Password(app):
#     app.forgot_your_password() #Проверка перехода на форму "Забыли пароль?"
#
# def test_Checkbox(app):
#     app.tick_activity() #Проверка активности "галочки"

# def test_VideoStreamOnline(app):
    # app.OnlinePageTestSuite.add_camera_player1() #Проверка добавления камеры в Плеер 1
    # app.OnlinePageTestSuite.add_camera_player2() #Проверка добавления камеры в Плеер 2
    # app.OnlinePageTestSuite.add_camera_player3() #Проверка добавления камеры в Плеер 3
    # app.OnlinePageTestSuite.add_camera_player4() #Проверка добавления камеры в Плеер 4

def test_ExpandScreenButton(app):
    app.OnlinePageTestSuite.expand_screen_button()


# def test_Archive(app):
#     # app.OnlinePageTestSuite.archive_search() #Проверка, что появился новый день с архивом
#     # app.OnlinePageTestSuite.archive_playback() #Проверка, что открылся плеер с архивом
#     app.OnlinePageTestSuite.download_archive() #Проверка, что скачался видеофайл архива

# def test_Localization(app):
#     app.Localization_RU.local()
