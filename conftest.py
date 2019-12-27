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







