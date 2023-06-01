import time

def func_1 (x: int):
    summ = 0
    for i in range(x):
        summ += i ** 4
    return summ
def timer(func, *args,**kwargs):
    statrt = time.time()
    resault = func(*args,**kwargs)
    stop = time.time()
    print('Time works function ',round(stop-statrt,4))
    return resault




print(timer(func_1,10000))



