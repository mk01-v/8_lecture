import string
import random

def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_new_project(app):
    # вход в аккаунт
        # ввод логина, пароля, нажатие кнопки вход.
    # создание проекта
        # Manage -> Manage Projects -> Кнопка Create New Project.
            # Указание имени проекта и описания.
    # проверка проекта создания проекта



































