def test_delete_fails(app):
    app.Monitoring.delete_txt()

def test_camera_CD100_E75A_ms3_dev(app):
    app.camera_CD100_E75A_ms3_dev.detection_of_archive()