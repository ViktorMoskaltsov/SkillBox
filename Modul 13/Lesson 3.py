class Infiniti :
    a = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a += 1
        return self.a

a = Infiniti()


for i in a
    print(i)
