import pytest
from fixture.Application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.Stop)
    return fixture
