class Parrents:
    def __init__(self, name, age, list_children):
        self.name = name
        self.age = age
        self.list_children = list_children

    def info_parent(self):
        print(f'Инофрмация о родителе\n1.Имя {self.name}\n2.Возраст {self.age}\n3.Список дитей {[c_name.name for c_name in self.list_children]}')

    def add_cildren(self, child):
        self.list_children.append(child)






class Children :
    def __init__(self, age_child, name, parent):
        self.age_child = age_child
        self.name = name
        self.parent = parent

        parent.add_cildren(self)

    def info_child(self):
        print(f'Ребенок {self.name} возрaст {self.age_child}')


parent_1 = Parrents('Виктор',26,[])

child_1 = Children(10, "Миша", parent_1)
parent_1.info_parent()

child_1.info_child()
