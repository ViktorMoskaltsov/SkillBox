price = []
n_price = int(input('введите кол во товоров : '))
for i in range (n_price) :
    print('Цена на товар ',end='')
    a = float(input())
    price.append(a)
first_procent = int(input('Процент в первый год : '))
second_procent = int(input('Процент в второй год : '))

first_yer = [i *(1+ first_procent/100) for i in price]
second_procent = [i * (1+ second_procent/100)for i in first_yer]

print('Сумма цен за каждый год ' , round(sum(price),2),round(sum(first_yer),2),round(sum(second_procent),2) )