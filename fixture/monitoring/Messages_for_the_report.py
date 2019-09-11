
class Messages:

    def __init__(self, app):
        self.app = app

    def Player_did_not_load_in_10_seconds(self):
        print('Не загрузилось видео за 10')
        with open('monitoring error report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" WARNING: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Плеер ' + str(
                    self.app.LineHours.hour) + ' не загрузился за 10 секунд.\n')
            f.close()

    def player_did_not_appear_in_15_seconds(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Плеер '+ str(self.app.LineHours.hour) +' не отобразился за 15 секунд.')
        with open('monitoring error report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" WARNING: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Плеер '+ str(self.app.LineHours.hour) +' не отобразился за 15 секунд.\n')
            f.close()

    def video_did_not_load_in_15_seconds(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка провалилась. Видео ' + str(
                self.app.LineHours.hour) + ' не загрузилось за 15 секунд.')
        with open('monitoring error report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" WARNING: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' не загрузилось за 15 секунд.\n')
            f.close()

    def video_download_and_the_duration_is_correct(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time).strip() + ' минут.')
        with open('monitoring report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" INFO: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time).strip() + ' минут.\n')
            f.close()

    def maximum_allowed_concurrent_connections_exceeded(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time).strip() + ' минут. Отображается сервисное сообщение - Превышено максимальное допустимое количество одновременный подключений.')
        with open('monitoring error report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a',
                  encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" WARNING: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time).strip() + ' минут. Отображается сервисное сообщение - Превышено максимальное допустимое количество одновременный подключений.\n')
            f.close()

    def motion_recording(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time).strip() + ' минут. Запись по детекции движения.')
        with open('monitoring report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" INFO: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time).strip() + ' минут. Запись по детекции движения.\n')
            f.close()

    def archive_duration_is_shorter(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Проверка прошла успешно. Видео ' + str(
                self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                self.app.Monitoring.archive_time).strip() + ' минут. !Длительность Архива меньше допустимой!')
        with open('monitoring error report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" WARNING: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Видео ' + str(
                    self.app.LineHours.hour) + ' загрузилось. Длительность видео ' + str(
                    self.app.Monitoring.archive_time).strip() + ' минут. !Длительность Архива меньше допустимой!\n')
            f.close()

    def no_archive_for_the(self):
        print(
            'Проверка для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Архива за ' + self.app.Date_determination.yesterday + ' число нет.')
        with open('monitoring error report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" WARNING: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Архива за ' + self.app.Date_determination.yesterday + ' число нет.\n')
            f.close()

    def no_archive(self):
        print(
            'Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
                self.app.LineHours.hour) + ' нет.')
        with open('monitoring error report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a',
                  encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" WARNING: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Архива ' + str(
                    self.app.LineHours.hour) + ' нет.\n')
            f.close()

    def there_is_no_scheduled_archive(self):
        print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
            self.app.LineHours.hour) + ' нет по расписанию.')
        with open('monitoring report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" INFO: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Архива ' + str(
                    self.app.LineHours.hour) + ' нет по расписанию.\n')
            f.close()

    def error_list_index_out_of_range(self, i):
        print(len(self.app.LineHours.list_elements), ' длина списка контейнеров с архивом.')
        self.len_list_elements = len(self.app.LineHours.list_elements)
        print(i,
              ' - инедекс, который подставляем в для поиска контейнера с архивом')  # Выводим индекс, чтобы отследить ошибку list index out of range
        with open('выявление ошибки LIST INDEX OUT OF RANGE ' + self.app.Monitoring.camera_name.strip() + '.txt',
                  'a',
                  encoding='utf-8') as f:
            f.write('' + str(i) + ' - инедекс, который подставляем в для поиска контейнера с архивом , ' + str(
                self.len_list_elements) + ' длина списка контейнеров с архивом. \n')
            f.close()

    def there_was_no_motion_detection(self):
        print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. Архива ' + str(
            self.app.LineHours.hour) + ' нет, т.к. не было никакого обнаружения движения.')
        with open('monitoring report ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write(
                '"' + self.app.Date_determination.strg_today + '" INFO: Проверка за '+ self.app.Date_determination.yesterday +' число для камеры "' + self.app.Monitoring.camera_name.strip() + '" выполнена. Архива ' + str(
                    self.app.LineHours.hour) + ' нет, т.к. не было никакого обнаружения движения.\n')
            f.close()

    def error_StaleElementReferenceException(self):
        print('Проверка, что открывается каждый контейнер с архивом за Вчерашний день. При проверки расписания для камеры "' + self.app.Monitoring.camera_name.strip() + '" произошла обработка ошибки StaleElementReferenceException.')
        with open('выявление ошибки StaleElementReferenceException ' + self.app.Monitoring.camera_name.strip() + '.txt', 'a', encoding='utf-8') as f:
            f.write('Произошла обработка ошибки StaleElementReferenceException.\n')
            f.close()