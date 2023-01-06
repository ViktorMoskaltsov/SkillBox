paks = []
decod = []
erors = 0

paks_count = int(input('Введите кол - во пакетов :' ))

for i_paks  in range (paks_count) :
    print('\nПакет номер ',i_paks+1)
    for i in range(4) :
        print(i+1,'Бит',end= ' ')
        bit = input()
        paks.append(bit)
    if paks.count(-1) > 1 :
        print('Много ощибок в пакете ')
        erors += 1
    else:
        decod.extend(paks)
    paks = []
print('\nПолученное сообщение ',decod)
print('Колличество ошибок ',erors)

