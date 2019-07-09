import pytest
import json
from fixture.Application import Application
import os.path


fixture = None
# target = None
#
# @pytest.fixture()
# def app(request):
#     global fixture
#     global target
#     if target is None:
#         config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target", default="target.json"))
#         with open(config_file) as f:
#             target = json.load(f)
#     if fixture is None or not fixture.is_valid():
#         fixture = Application()
#     return fixture

@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# def oytest_addoption(parser):
#     parser.addoption("--target", action="store", defaut="target.json")