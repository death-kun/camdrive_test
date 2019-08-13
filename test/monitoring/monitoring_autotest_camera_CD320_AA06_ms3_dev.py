def test_delete_fails(app):
    app.Monitoring.delete_txt()

def test_camera_CD320_AA06_ms3_dev(app):
    app.camera_CD320_AA06_ms3_dev.detection_of_archive()