from model.project import Project

def test_new_project(app):
    # вход в аккаунт
        # ввод логина, пароля, нажатие кнопки вход.
    username = "administrator"
    password = "root"
    app.session.login(username, password)

    # создание проекта
    project = Project(name="namepr1", description="namedisc1")
    app.project.create_project(project)

    # проверка проекта создания проекта
    # assert ****

    