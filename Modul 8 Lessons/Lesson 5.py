import copy

a = [[1,2,3],2,3,]
b = []

b = copy.deepcopy(a)

a[0][0] =10

print(a)

print(b)