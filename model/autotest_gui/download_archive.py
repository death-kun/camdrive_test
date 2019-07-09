
class downloadarchive:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        self.app.Monitoring.delete_txt()
        self.app.open_home_page()
        self.app.login_autotest()
        self.app.Camera_List.click_camera_CD_120()
        self.app.Archive.open_archive()
        # Проверка есть ли в папке Downloads файл с расширением avi и удаляет его
        self.app.Archive.delete_avi()
        self.app.Archive.video_archive_fragment_download()
        # Проверка, что скачался видеофайл архива
        self.app.Archive.search_avi()
        self.app.logout_butten()
