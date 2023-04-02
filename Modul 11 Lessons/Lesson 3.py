class Family:
    famili_name = 'Moskaltsov'
    money = 10**5

    house = False
    def info (self):
        print('Family : {}\nFamily funds : {}\nHouse : {}\n'.format(self.famili_name,self.money,self.house))
    def ern_mony (self,amount):
        self.money += amount
        print('Заработали {} ,всего денег {}'.format(amount,self.money))
    def by_house (self,house_price,discont = 0):
        house_price -= house_price * discont /100
        if self.money >= house_price :
            self.house = True
            self.money -= house_price
            print('Дом куплен . Остаток денег {}\n'.format(self.money))
        else:
            print('Не хватает денег\n')

name = Family()
name.info()
name.ern_mony(850000)
name.by_house(10**6,20)