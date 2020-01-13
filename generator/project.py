from model.project import Project
import random
import string
import os.path
import jsonpickle
#import json
# для чтения опций командной строки (getopt).
# sys для получения доступа к этим опциям (sys).
import getopt
import sys

# параметризованный генератор.
# Пример из официальной документации как читать опции из командной строки.
# преобразование в комфортный вид.
# "n:f:" - кол-во генерации, в какой файл.
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

#анализ параметров.
n = 4
f = "data/projects.json"
# как устроена переменная opts прочитанная парсером getopt.
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
# в edit configuration - Parametrs - указываем "-n 10 -f data/test.json"
# создает 10 групп (11, т.к. + без значений) и  помещает в файл test.json.


# генератор данных.
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits # + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#Вводимые данные
testdata = [Project(name="1_name", description="1_description")] + [
    Project(name=random_string("name", 10), description=random_string("description", 10))
    for i in range(n)
]

# вывод данных в файл json "groups.json".
# ".." переход на 2 уровня выше
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    # записывает данные в файл тестовых данных, импорт нужен json, _dict_ дефолт настройки для преобразования данных и
    # .. и превращаем в словарь. Indent для вывода строк в столбец
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    # jsonpickle - была проблема восстановить обратно объект по этим данным и заполнятся нужными свойствами. Расширение json.
    # преобразовывать произвольные объекты в формат json и обратно.
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))