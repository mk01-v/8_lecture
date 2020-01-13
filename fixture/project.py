from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd

        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)

        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def delete_project(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.open_project_page()
        # сбрасываем кэш, т.к. после операции является не валидным.
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.project_cache = []
            self.open_project_page()
            # выбор таблицы, если несколько [2].
            table = wd.find_elements_by_tag_name("table")[2]
            # поиск по строкам.
            for row in table.find_elements_by_css_selector('tr.row-1, tr.row-2'):
                # поиск по элементам.
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[1].text
                href = row.find_element_by_css_selector("a").get_attribute("href")
                id = href[70:]
                self.project_cache.append(Project(name=name, description=description, id=id))
        return list(self.project_cache)
