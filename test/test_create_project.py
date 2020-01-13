from model.project import Project

def test_new_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)

    # создание проекта
    old_projects = app.project.get_project_list()
    project = Project(name="name_123", description="description_123")
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
