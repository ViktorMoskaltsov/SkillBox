import random

fst_1 = [random.randint(50 , 80) for _ in range(10)]
scd_2 = [random.randint(30 , 60) for _ in range(10)]

sqad = [('Погиб 'if fst_1[dm] + scd_2[dm] > 100 else 'Выжил ' ) for dm in range(10)]

print(fst_1)
print(scd_2)

print(sqad)
