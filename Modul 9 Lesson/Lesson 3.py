import os

path_to_first = os.path.abspath(os.path.join(os.path.sep,'task', 'group_1.txt'))
path_to_second = os.path.abspath(os.path.join(os.path.sep,'task', 'Additional_info', 'group_2.txt'))
file = open(path_to_first, 'r', encoding='utf8')
file_2 = open(path_to_second, 'r', encoding='utf8')

summa = 0
diff = 0
compose = 1

for i_line in file:
    info = i_line.split()
    if info:
        summa += int(info[2])
        diff -= int(info[2])

for i_line in file_2:
    info = i_line.split()
    if info:
        compose *= int(info[2])

file.close()
file_2.close()

print(summa)

print(diff)

print(compose)