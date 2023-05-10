
class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class WarRobot(Robot):

    def __init__(self, gun, model):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print(f'Робот {self.model} охраняет военный обьект при помощи {self.gun}')


class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        super().operate()
        self.garbage_bag += 1
        print(f'Робот пылесосит пол,заполниность пылесоса {self.garbage_bag}')


class SubmarineRobot(WarRobot):

    def __init__(self, gun, model, depth):
        super().__init__(gun, model)
        self.depth = depth

    def operate(self):
        super().operate()
        print('Охрана ведется под водой на глубине', self.depth)

a = WarRobot(7.62,'Mark')
a.operate()
b = SubmarineRobot(7.62,'Tom',777)
b.operate()
c = VacuumCleaningRobot('Xiomi')
c.operate()