def test_delete_fails(app):
    app.Monitoring.delete_txt()

def test_camera_CD100_E778_ms5(app):
    app.camera_CD100_E778_ms5.detection_of_archive()