import pytest

def test_delete_fails(app):
    app.Monitoring.delete_txt()

@pytest.mark.xfail(reason=False)
def test_camera_CD120_D521(app):
    app.camera_CD120_D521.detection_of_archive()

@pytest.mark.xfail(reason=False)
def test_camera_CD_120(app):
    app.camera_CD_120.detection_of_archive()


