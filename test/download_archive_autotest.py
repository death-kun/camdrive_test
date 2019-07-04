
def test_Archive(app):
    app.download_archive.autotest()

def delete_fails(app):
    app.delete_txt()