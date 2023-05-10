class Ships:
    def __init__(self,model):
        self.model = model

    def __str__(self):
        return f'\nModel Ship {self.model}'

    def swim(self):
        print('\nКорабль движется ')

class WarShip(Ships):
    def __init__(self,model,gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print(f'\nShip {self.model} attack from gun {self.gun}')

class CargoShip(Ships):
    def __init__(self,model):
        super().__init__(model)
        self.tonnage = 0


    def load(self):
        self.tonnage += 1
        print('\nLoad Ship')
        print('current workload ',self.tonnage)

    def unload(self):
        print('\nРазгружаем корабль')
        if self.tonnage > 0 :
            self.tonnage -= 1
        else:
            print('Корабль уже разгружен')
        print('current workload ',self.tonnage)


batellship = WarShip('McDonald','BushMaster')
cargo = CargoShip('FairFox')
print(cargo)
cargo.swim(),cargo.load(),cargo.load(),cargo.unload()
print(batellship)
batellship.swim(),batellship.attack()