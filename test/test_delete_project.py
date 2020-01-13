from model.project import Project
import random


def test_delete_project_without_soap(app):

    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="test", description="qweqwe"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def test_delete_project_with_soap(app):

    if len(app.soap.get_project_list_soap("administrator", "root")) == 0:
        app.project.create_project(Project(name="test", description="qweqwe"))
    old_projects = app.soap.get_project_list_soap("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    new_projects = app.soap.get_project_list_soap("administrator", "root")
    old_projects.remove(project)
    assert old_projects == new_projects
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
