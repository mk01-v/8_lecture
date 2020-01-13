from model.project import Project
import random


def test_delete_project(app):
    # вход в аккаунт
    # ввод логина, пароля, нажатие кнопки вход.
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")

    old_projects = app.soap.get_project_list("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project(project.id)


