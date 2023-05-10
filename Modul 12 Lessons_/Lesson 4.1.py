class Unit:

    def __init__(self, hp):
        self.__hp = hp

    def set_hp(self, amount):
        self.__hp = amount

    def get_hp(self):
        return self.__hp

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - 0)  # -0 написан для наглядности, в теории  мы могли бы этого и не писать

class Soldier(Unit):

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount)
    def __str__(self):
        return f'хп {self.get_hp()} урон {self.set_hp()}'

class Citizen(Unit):
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount * 2)

s = Soldier(hp=100)
s.set_hp(20)

s.get_damage(20)
print(s)