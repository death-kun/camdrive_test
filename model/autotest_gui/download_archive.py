
class DownloadArchive:

    def __init__(self, app):
        self.app = app

    def autotest(self):
        self.app.DeleteTxtFiles.delete_txt()
        self.app.Authorization.open_home_page()
        self.app.Authorization.login_autotest()
        self.app.CameraList.click_camera_CD_120()
        self.app.Archive.open_archive()
        # Проверка есть ли в папке Downloads файл с расширением avi и удаляет его
        self.app.Archive.delete_avi()
        self.app.Archive.video_archive_fragment_download()
        # Проверка, что скачался видеофайл архива
        self.app.Archive.search_avi()
        self.app.Authorization.logout_butten()
