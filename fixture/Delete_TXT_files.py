from pathlib import Path

class DeleteTxtFile:
    def __init__(self, app):
        self.app = app

    def delete_txt(self):
        txt_files = Path('.').glob('*.txt')
        for f in txt_files:
            Path.unlink(f)