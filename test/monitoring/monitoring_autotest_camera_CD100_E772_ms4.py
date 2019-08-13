def test_delete_fails(app):
    app.Monitoring.delete_txt()

def test_camera_CD100_E772_ms4(app):
    app.camera_CD100_E772_ms4.detection_of_archive()