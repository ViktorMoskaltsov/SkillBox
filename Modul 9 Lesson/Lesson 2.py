import os

def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result




trec = input('Введите путь : ')
name_file = input('Введите фаайл ')

find_file(trec,name_file)