def is_film_exist (movie,films_list) :
    for i_movie in films_list :
        if i_movie == movie :
            return True
    return False





films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]
comand_list = ['добавить','вствить ','удлить']
top_list = []
while True :
    print('Вш текущий топ фильмов ',top_list)
    entr_film = input('Название фильм : ')
    if is_film_exist(entr_film,films):
        print('Комнды добавить , удалить , вставить ')
        comand = input("Введите команду : ")
        if comand == 'добавить' :
            top_list.append(entr_film)
        if comand == 'удалить' :
            if is_film_exist(entr_film,top_list) :
                top_list.remove(entr_film)
            else:
                print('Такого фильма нет в нашем топе !')
        if comand == 'вставить' :

            index = int(input('На какое место в списке вствить : '))
            top_list.insert(index-1,entr_film)


    else:
        print('Такова фильма нет на сайте ')