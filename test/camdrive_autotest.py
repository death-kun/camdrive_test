#
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
#
# def test_VideoStreamOnline(app):
#     app.Player.add_camera_player1() #Проверка добавления камеры в Плеер 1
#     app.Player.add_camera_player2() #Проверка добавления камеры в Плеер 2
#     app.Player.add_camera_player3() #Проверка добавления камеры в Плеер 3
#     app.Player.add_camera_player4() #Проверка добавления камеры в Плеер 4
#
# def test_ExpandScreenButton(app):
#     app.Player.expand_screen_button() #Проверка, что плеер открылся в формате 1х1
#     app.Player.roll_up_screen_button() #Проверка, что плеер открылся в формате 1х4

# def test_Camera_Tree_Change_Buttons(app):
#     app.TopEditButtons.add_camera_button() #Проверка, что открылась Форма добавления камеры
#     app.TopEditButtons.remove_camera_button() #Проверка, что открылась Форма удаления камеры
#     app.TopEditButtons.camera_rename_button() #Проверка, что изменилось имя камеры

# def test_Group_Tree_Change_Buttons(app):
    # app.BottomEditButtons.add_group() #Проверка, что добавлеена Новая группа
    # app.BottomEditButtons.rename_group() #Проверка, что изменилось имя Группы
    # app.BottomEditButtons.group_deletion() #Проверка, что Новая группа удалена

# def test_Archive(app):
#     app.Archive.archive_search() #Проверка, что появился новый день с архивом
#     app.Archive.archive_playback() #Проверка, что открылся плеер с архивомЫ
#     app.Archive.download_archive() #Проверка, что скачался видеофайл архива

# def test_Localization(app):
#     app.Localization_RU.local()

def test_monitoring(app):
    app.Monitoring.archive_length_determination()