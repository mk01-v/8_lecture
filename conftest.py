from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture


#Для быстрого запуска - в рамках одной сессии.
#@pytest.fixture(scope = 'session')
#Для медленного запуска, сессия создается заново при инициализации теста.
#pytest.fixture

#@pytest.fixture(scope = 'session')
#def app(request):
#    fixture = Application()
#    fixture.session.login(username="admin", password="secret")
#    def fin():
#        fixture.session.logout()
#        fixture.destroy()
#    request.addfinalizer(fin)
#    return fixture

fixture = None
target = None

# отдельная функция по запуску БД.
def load_config(file):
    global target
    # не забыть указать корень директории проекта, иначе не будет работать target.json
    # *запуск проектов* - edit configuration - working directory.
    # C:\Python\Projects\2_lecture_2_homework
    if target is None:
        # прописывание директории по-умолчанию, т.к. не цеплялся файл json к проекту.
        # 1 - abspath преоброзование в абсолютный путь, 2 dirname получили директорию, 3 - к этой директории приклеиваем ..
        # .. путь к конфигурационному файлу join. 4 - то что собираемся подклеить request.config.getoption("--target").
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

# запуск веба без БД.
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid:
        fixture = Application(browser=browser, base_Url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

# срабатывание всегда из-за autouse.
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# Зацепка (hook). Добавляет доп. параметр. 1 параметр добавляем браузер, 2 действие - сохранить, 3 по умолчанию.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

# в test_add_group проверяется наименование, в зависимости от выбранных условий подставляются данные.
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            # 1 - куда будут подставляться параметры, 2 - какие значения подставляем, 3 - строковое представление.
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

# фикстура для БД, запуск из файла.
@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
        request.addfinalizer(fin)
    return dbfixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")







