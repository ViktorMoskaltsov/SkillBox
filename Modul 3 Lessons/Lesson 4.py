goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт : ')
price = int(input('Цена : '))
new_frutt = []

new_frutt.append(fruit_name)
new_frutt.append(price)
goods.append(new_frutt)

print('Новый список ',goods)

for i in range (len(goods)) :
    goods[i][1] = (goods[i][1] * 8 )/100 + goods[i][1]

print('Список новых цен',goods)
