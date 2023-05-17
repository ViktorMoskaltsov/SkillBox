class Iterator :
    def __init__(self,a):
        self.a = a

    def iter_my(self):
        b = len(self.a)
        while b == len(self.a) :
            b -= 1
            print(self.a)
            self.a.reverse()
            print(self.a[b])
            self.a.pop(b)
            self.a.reverse()
            b += 1
            if  self.a == []:
                raise StopIteration('Стоп итератор')

itera = Iterator([1,2,3,4,6])


for _ in range(5):
    itera.iter_my()
