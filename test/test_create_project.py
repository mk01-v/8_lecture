from model.project import Project

def test_new_project(app):
    # вход в аккаунт
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    project = Project(name="namepr1", description="namedisc1")
    app.project.create_project(project)

        # ввод логина, пароля, нажатие кнопки вход.
    # создание проекта
        # Manage -> Manage Projects -> Кнопка Create New Project.
            # Указание имени проекта и описания.
    # проверка проекта создания проекта



































