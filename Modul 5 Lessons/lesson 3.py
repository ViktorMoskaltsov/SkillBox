while True :
    happy_text = input('Введите шаблон поздравления, в шаблоне нужно использовать конструкцию {name} и {age}:')
    if '{name}' in happy_text and '{age}' in happy_text :
        break
    print('Ошибка ввода тест должен содержать конструкцию {name} и {age} !')

neme_list = input('Список людей через зяпятую ').split(',')
age_list = input('Возрвст людей через зяпятую ').split(',')

for i in range(len(neme_list)) :
    print(happy_text.format(name= neme_list[i],age = age_list[i]))

people = [' '.join([neme_list[i],age_list[i]])
          for i in range(len(neme_list))]
people = ' '.join(people)
print('\nИмениники ',people)