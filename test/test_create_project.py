from model.project import Project

def test_new_project_without_soap(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)

    # создание проекта
    old_projects = app.project.get_project_list()
    project = Project(name="name_123", description="description_123")
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)


def test_new_project_load_projectjson_soap(app, json_projects):
    username = "administrator"
    password = "root"
    #app.session.login(username, password)
    app.session.ensure_login(username, password)
    project_json = json_projects
    old_projects = app.soap.get_project_list_soap(username, password)
    app.project.create_project(project_json)
    new_projects = app.soap.get_project_list_soap(username, password)
    assert len(old_projects) + 1 == len(new_projects)

