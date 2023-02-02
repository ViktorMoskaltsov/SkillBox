def dict_hist (string) :
    for i in string :
        sym_dict = dict()
        for i in string :
            if i in sym_dict :
                sym_dict[i] += 1
            else:
                sym_dict[i] = 1
    return sym_dict


text = input('Введите текст :').lower()

hist = dict_hist(text)
for i in sorted(hist.keys()) :
    print(i, ' : ',hist[i])


print('Максимальная чистота ',max(hist.values()))