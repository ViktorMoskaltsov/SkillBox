class Point :
    __count = 0
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.set_x(x)
        self.set_y(y)
        Point.__count += 1

    def __str__(self):
        return f'Point number {self.__count}\nx = {self.__x}\ty = {self.__y} '

    def get_x (self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self,x):
        if isinstance(self.__x,int):
            self.__x = x
        else:
            raise Exception('Координата ч не является числом ')
    def set_y(self,y):
        if isinstance(self.__y,int):
            self.__y = y
        else:
            raise Exception('Координата у  не является числом ')
point = Point(1,3)
print(point)
point_2 = Point(2,444444444)
print(point_2)
print(point_2.get_y())
