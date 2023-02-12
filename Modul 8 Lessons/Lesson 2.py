site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}

def faind_key (structur,key) :
    if key in structur:
        return structur[key]
    for i_value in structur.values():
        if isinstance(i_value,dict):
            resault = faind_key(i_value,key)
            if resault:
                break
    else:
        resault = None

    return resault






key_user = input('Введите ключ :')
value = faind_key(site,key_user)
if value:
    print(value)

else:
    print('Таоква ключа не существует !!')



# Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по ней и найти нужный элемент.
# Для этого в программировании используются специальные алгоритмы поиска.
#
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран.
# В качестве примера можно использовать такой словарь: