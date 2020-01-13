from model.project import Project
import random


def test_delete_project_without_soap(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects

def test_delete_project_with_soap(app):
    # вход в аккаунт
    # ввод логина, пароля, нажатие кнопки вход.
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects = app.soap.get_project_list_soap("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    new_projects = app.soap.get_project_list_soap("administrator", "root")
    old_projects.remove(project)
    assert old_projects == new_projects

