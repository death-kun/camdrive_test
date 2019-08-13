def test_delete_fails(app):
    app.Monitoring.delete_txt()

def test_camera_N1001_3A00_bwd(app):
    app.camera_N1001_3A00_bwd.detection_of_archive()