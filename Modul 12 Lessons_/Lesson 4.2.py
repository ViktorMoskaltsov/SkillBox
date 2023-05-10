class CanFly:
    h = 0
    speed = 0

    def up(self):
        pass
    def flying(self):
        pass
    def down(self):
        self.h = 0
        self.speed = 0

    def __str__(self):
        return f'Высота {self.h}\tCкорость {self.speed}'

class Batterflyi(CanFly):
    def up(self):
        self.h = 1
        self.speed = 0.5
    def __str__(self):
        info = super().__str__()
        info = '\n'.join(('Бабочка летит',info))
        return info
class Rocet(CanFly):
    bomb = True
    def up(self):
        self.h = 500
        self.speed = 1000

    def down(self):
        self.h = 0
        self.speed = 0
        self.bomb = False
    def __str__(self):
        info = super().__str__()


        if self.bomb == True :
            info = '\n'.join(('Рокета летит',info))
            return info
        else:
            info = '\n'.join(('Взрыв Рокеты',info))
            return info

batter = Batterflyi()
batter.up()
print(batter)
rock = Rocet()
rock.up()
print(rock)
rock.down()
print(rock)