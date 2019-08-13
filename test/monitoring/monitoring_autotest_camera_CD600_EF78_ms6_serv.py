def test_delete_fails(app):
    app.Monitoring.delete_txt()

def test_camera_CD600_EF78_ms6_serv(app):
    app.camera_CD600_EF78_ms6_serv.detection_of_archive()