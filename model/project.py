from sys import maxsize


class Project:

    def __init__(self, name=None, description=None, id=None):
        self.name = name
        self.description = description
        self.id = id

    #вывод содержимое объектов, а не адресов памяти. Строковое представление в консоли.
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.discription)

    # чтобы не сравнивал по физическому расположению, а сравнивал логически - индификаторы и имена.
    # необходимо для сравнения самих объектов.
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize