ip_address = '{0}.{1}.{2}.{3}'
count = 0
num = []
while True:
    new_num = int(input('Введите число '))
    if 0 <= new_num <= 255 :
        num.append(new_num)
        count+= 1
        if count == 4 :
            break
    else:
        print('Ошибка ввода , число от 0 жо 255 ')
        count = 0
        num = []
        print('Начните ввод занова')
print(ip_address.format(*num))
