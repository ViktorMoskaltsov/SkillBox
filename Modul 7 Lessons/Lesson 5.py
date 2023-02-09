phone_book = dict()

while True :
    name = input('Введите имя :')
    fst_name = input('Введите фамилию :')
    name_fst_name = (name, fst_name)

    if name_fst_name in phone_book :
        print('Такой контакт уже существует'
        )
        break
    else:
        phone = int(input('Введите номер телефона :'))

        phone_book[name_fst_name] = phone

print(phone_book)