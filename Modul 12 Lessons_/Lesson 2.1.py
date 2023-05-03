class Hueman :
    __count = 0
    def __init__(self,name,age):
        self.set_age(age)
        self.set_name(name)

    def __str__(self):
        return f'Name {self.__name}\t Age {self.__age}'

    def set_age(self,age):
        if age in range(1,100):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')
    def set_name(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            raise Exception('Имя должно состоять из букв')
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

anna = Hueman('Anna',20)
anna.set_age(22)
print(anna)
