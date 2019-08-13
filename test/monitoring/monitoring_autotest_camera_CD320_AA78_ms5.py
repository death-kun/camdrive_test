def test_delete_fails(app):
    app.Monitoring.delete_txt()

def test_camera_CD320_AA78_ms5(app):
    app.camera_CD320_AA78_ms5.detection_of_archive()