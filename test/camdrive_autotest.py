
# def test_log_in(app):
#     app.Authorization.login_with_incorrect_data() #Проверка того, что указан не верный пароль
#     app.Authorization.password_visibility_check() #Проверка, что при нажатии на "глаз" видно введенный пароль
#     app.Authorization.login_with_valid_data() #Проверка того, что указан верный логин и пароль
#
# def test_forgot_your_password(app):
#     app.forgot_your_password() #Проверка перехода на форму "Забыли пароль?"
#
# def test_checkbox(app):
#     app.tick_activity() #Проверка активности "галочки"

def test_Online_Page(app):
    # app.OnlinePageTestSuite.add_camera_player1() #Проверка добавления камеры в Плеер 1
    # app.OnlinePageTestSuite.add_camera_player2() #Проверка добавления камеры в Плеер 2
    # app.OnlinePageTestSuite.add_camera_player3() #Проверка добавления камеры в Плеер 3
    # app.OnlinePageTestSuite.add_camera_player4() #Проверка добавления камеры в Плеер 4
    # app.OnlinePageTestSuite.archive_search() #Проверка, что появился новый день с архивом
    # app.OnlinePageTestSuite.archive_playback() #Проверка, что открылся плеер с архивом
    app.OnlinePageTestSuite.download_archive() #Проверка, что скачался видеофайл архива