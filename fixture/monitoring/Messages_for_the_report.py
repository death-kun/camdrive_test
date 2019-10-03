
class Messages:

    def __init__(self, app):
        self.app = app

    def Player_did_not_load_in_10_seconds(self):
        print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Плеер ' + str(
                self.app.LineHours.hour) + ' не загрузился за 10 секунд.')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Плеер ' + str(
                    self.app.LineHours.hour) + ' не загрузился за 10 секунд.\n')
            f.close()

    def player_did_not_appear_in_15_seconds(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Плеер '+ str(self.app.LineHours.hour) +' не отобразился за 15 секунд.')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Плеер '+ str(self.app.LineHours.hour) +' не отобразился за 15 секунд.\n')
            f.close()

    def video_did_not_load_in_15_seconds(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Видео ' + str(
                self.app.LineHours.hour) + ' не загрузилось за 15 секунд.')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' не загрузилось за 15 секунд.\n')
            f.close()

    def video_download_and_the_duration_is_correct(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time) + ' минут.')
        with open('monitoring report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time) + ' минут.\n')
            f.close()

    def maximum_allowed_concurrent_connections_exceeded(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time) + ' минут. Отображается сервисное сообщение - Превышено максимальное допустимое количество одновременных подключений.')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a',
                  encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time) + ' минут. Отображается сервисное сообщение - Превышено максимальное допустимое количество одновременных подключений.\n')
            f.close()

    def motion_recording(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time) + ' минут. Запись по детекции движения.')
        with open('monitoring report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time) + ' минут. Запись по детекции движения.\n')
            f.close()

    def archive_duration_is_shorter(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time) + ' минут. !Длительность Архива меньше допустимой!')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time) + ' минут. Длительность Архива меньше допустимой!\n')
            f.close()

    def no_archive_for_the(self):
        print(
            'Проверка для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Архива за ' + self.app.DateDetermination.yesterday + ' число нет.')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Архива за ' + self.app.DateDetermination.yesterday + ' число нет.\n')
            f.close()

    def no_archive(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
                self.app.LineHours.hour) + ' нет.')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a',
                  encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Архива ' + str(
                    self.app.LineHours.hour) + ' нет.\n')
            f.close()

    def there_is_no_scheduled_archive(self):
        print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
            self.app.LineHours.hour) + ' нет по расписанию.')
        with open('monitoring report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Архива ' + str(
                    self.app.LineHours.hour) + ' нет по расписанию.\n')
            f.close()

    def error_list_index_out_of_range(self, i):
        print(len(self.app.LineHours.list_elements), ' длина списка контейнеров с архивом.')
        self.len_list_elements = len(self.app.LineHours.list_elements)
        print(i,
              ' - инедекс, который подставляем в для поиска контейнера с архивом')  # Выводим индекс, чтобы отследить ошибку list index out of range
        with open('выявление ошибки LIST INDEX OUT OF RANGE ' + self.app.Schedule.camera_name_shedule + '.txt',
                  'a',
                  encoding='utf-8') as f:
            f.write('' + str(i) + ' - инедекс, который подставляем в для поиска контейнера с архивом , ' + str(
                self.len_list_elements) + ' длина списка контейнеров с архивом. \n')
            f.close()

    def there_was_no_motion_detection(self):
        print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
            self.app.LineHours.hour) + ' нет, т.к. не было никакого обнаружения движения.')
        with open('monitoring report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. Архива ' + str(
                    self.app.LineHours.hour) + ' нет, т.к. не было никакого обнаружения движения.\n')
            f.close()

    def error_StaleElementReferenceException(self):
        print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. При проверки расписания для камеры "' + self.app.Schedule.camera_name_shedule + '" произошла обработка ошибки StaleElementReferenceException.')
        with open('выявление ошибки StaleElementReferenceException ' + self.app.Schedule.camera_name_shedule + '.txt', 'a', encoding='utf-8') as f:
            f.write('Произошла обработка ошибки StaleElementReferenceException.\n')
            f.close()

    def download_the_desired_archive_file(self):
        print('Скачался нужный файл.')
        with open('download archive report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Скачался нужный файл архива. Скачался ' + str(
                    self.app.Archive.avi_file) + '.\n')
            f.close()

    def wrong_archive_file_downloaded(self):
        print("Скачался не тот файл.")
        with open('download archive error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Скачался не тот файл архива. Скачался ' + str(
                    self.app.Archive.avi_file) + '.\n')
            f.close()

    def wrong_camera_selected(self):
        print('!!!ОШИБКА СЕРВЕРА!!! Выбранная камера не совпадает с камерой для, которой проходит тест')
        with open('monitoring error report ' + self.app.Schedule.camera_name_shedule + '.txt', 'a',
                  encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка за '+ self.app.DateDetermination.yesterday +' число для камеры "' + self.app.Schedule.camera_name_shedule + '" выполнена. При переходе на Расписание произошла ошибка сервера и была выбрана камера '+ self.app.Monitoring.camera_name +'.\n')
            f.close()

    def player1_added(self):
        print('Проверка добавления камеры в Плеер 1. Проверка прошла успешно. Добавлена камера в Плеер 1')
        with open('top edit buttons report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка добавления камеры в Плеер 1 прошла успешно. Добавлена камера в Плеер 1.\n')
            f.close()

    def player2_added(self):
        print('Проверка добавления камеры в Плеер 2. Проверка прошла успешно. Добавлена камера в Плеер 2')
        with open('top edit buttons report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка добавления камеры в Плеер 2 прошла успешно. Добавлена камера в Плеер 2.\n')
            f.close()

    def player3_added(self):
        print('Проверка добавления камеры в Плеер 3. Проверка прошла успешно. Добавлена камера в Плеер 3')
        with open('top edit buttons report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка добавления камеры в Плеер 1 прошла успешно. Добавлена камера в Плеер 1.\n')
            f.close()

    def player4_added(self):
        print('Проверка добавления камеры в Плеер 4. Проверка прошла успешно. Добавлена камера в Плеер 4')
        with open('top edit buttons report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка добавления камеры в Плеер 4 прошла успешно. Добавлена камера в Плеер 4.\n')
            f.close()

    def no_player4_added(self):
        print('Проверка добавления камеры в Плеер 4. Проверка провалилась. Камера не добавлена в Плеер 4')
        with open('top edit buttons error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка добавления камеры в Плеер 4 провалилась. Камера не добавлена в Плеер 4.\n')
            f.close()

    def no_player3_added(self):
        print('Проверка добавления камеры в Плеер 3. Проверка провалилась. Камера не добавлена в Плеер 3')
        with open('top edit buttons error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка добавления камеры в Плеер 3 провалилась. Камера не добавлена в Плеер 3.\n')
            f.close()

    def no_player2_added(self):
        print('Проверка добавления камеры в Плеер 4. Проверка провалилась. Камера не добавлена в Плеер 2')
        with open('top edit buttons error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка добавления камеры в Плеер 2 провалилась. Камера не добавлена в Плеер 2.\n')
            f.close()

    def no_player1_added(self):
        print('Проверка добавления камеры в Плеер 4. Проверка провалилась. Камера не добавлена в Плеер 1')
        with open('top edit buttons error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка добавления камеры в Плеер 1 провалилась. Камера не добавлена в Плеер 1.\n')
            f.close()

    def camera_add_form_is_open(self):
        print('Проверка, что открылась Форма добавления камеры. Проверка прошла успешно. Открылась Форма добавления камеры')
        with open('top edit buttons report.txt', 'a', encoding='utf-8') as f:
            f.write('"' + self.app.DateDetermination.strg_today + '" INFO: Проверка, что открылась Форма добавления камеры прошла успешно. Открылась Форма добавления камеры.\n')
            f.close()

    def camera_add_form_is_not_open(self):
        print('Проверка, что открылась Форма добавления камеры. Проверка провалилась. Форма добавления камеры не открылась')
        with open('top edit buttons error report.txt', 'a', encoding='utf-8') as f:
            f.write('"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка, что открылась Форма добавления камеры провалилась. Форма добавления камеры не открылась.\n')
            f.close()

    def camera_delete_form_is_open(self):
        print(
            'Проверка, что открылась Форма удалени камеры. Проверка прошла успешно. Открылась Форма удаления камеры')
        with open('top edit buttons report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка, что открылась Форма удаления камеры прошла успешно. Открылась Форма удаления камеры.\n')
            f.close()

    def camera_delete_form_is_not_open(self):
        print(
            'Проверка, что открылась Форма удаления камеры. Проверка провалилась. Форма удаления камеры не открылась')
        with open('top edit buttons error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка, что открылась Форма удаления камеры провалилась. Форма удаления камеры не открылась.\n')
            f.close()

    def camera_renamed(self):
        print('Проверка, что изменилось имя камеры. Проверка прошла успешно. Камера переименована')
        with open('top edit buttons report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка, что изменилось имя камеры прошла успешно. Камера переименована.\n')
            f.close()

    def camera_not_renamed(self):
        print('Проверка, что изменилось имя камеры. Проверка прошла успешно. Камера переименована')
        with open('top edit buttons error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка, что изменилось имя камеры провалилась. Камера не переименована.\n')
            f.close()

    def authorization_was_successful(self):
        print(
            'Проверка того, что указан верный логин и пароль. Проверка прошла успешно. Логин и пароль введены корректно')
        with open('authorization report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка, что после ввода корректного логина и пароля происходит авторизация прошла успешно. Открылся личный кабинет пользователя.\n')
            f.close()

    def authorization_failed(self):
        print('Проверка того, что указан верный логин и пароль. Проверка провалилась. Данные введены некорректно')
        with open('authorization error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка, что после ввода корректного логина и пароля происходит авторизация провалилась. Авторизация не произошла.\n')
            f.close()

    def incorrect_login_entered(self):
        print('Проверка того, что указан не верный пароль. Проверка прошла успешно. Введен некорректный логин')
        with open('authorization report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка, что после ввода не корректного логина не происходит авторизация прошла успешно. Отобразилась надпись "Ошибка идентификации".\n')
            f.close()

    def correct_login_entered(self):
        print('Проверка того, что указан не верный пароль. Проверка провалилась. Введены корректные значения')
        with open('authorization error report.txt', 'a', encoding='utf-8') as f:
            f.write(
            '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка, что после ввода не корректного логина не происходит авторизация провалилась. Сообщение "Ошибка идентификации" не появилось.\n')
            f.close()

    def incorrect_password_entered(self):
        print('Проверка того, что указан не верный пароль. Проверка прошла успешно. Введен некорректный пароль')
        with open('authorization report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" INFO: Проверка, что после ввода не корректного пароля не происходит авторизация прошла успешно. Отобразилась надпись "Ошибка идентификации".\n')
            f.close()

    def correct_password_entered(self):
        print('Проверка того, что указан не верный пароль. Проверка провалилась. Введены корректные значения')
        with open('authorization error report.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.DateDetermination.strg_today + '" WARNING: Проверка, что после ввода не корректного пароля не происходит авторизация провалилась. Сообщение "Ошибка идентификации" не появилось.\n')
            f.close()
