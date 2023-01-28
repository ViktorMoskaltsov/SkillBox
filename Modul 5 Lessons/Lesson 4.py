text_list = input('Введите текст : ')
up = [u for u in text_list if u.isupper()]
low = [l for l in text_list if l.islower()]
if len(low) > len(up) :
    print(text_list.lower())
else:
    print(text_list.upper())