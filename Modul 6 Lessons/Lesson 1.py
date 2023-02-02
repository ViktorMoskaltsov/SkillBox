
phone_dict = dict()
while True :
    print('Текущие когтакты на телефоне :')
    print('Выход end ')
    print(phone_dict)
    phone = input('Введите имя')
    if phone in phone_dict :
        print('ошибка такой контакт уже существует')
    if phone == 'end' :
        break
    else:
        contatct = int(input('Введите номер контакта '))
        phone_dict[phone] = contatct