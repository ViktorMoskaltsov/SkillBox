players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}
players_a_rest = [i['name']for i in players_dict.values()
                  if i['team'] == 'A' and i['status'] == 'Rest']
players_b_trening = [i['name']for i in players_dict.values()
                  if i['team'] == 'B' and i['status'] == 'Training']
players_c_travel = [i['name']for i in players_dict.values()
                  if i['team'] == 'C' and i['status'] == 'Travel']

print('Все члены команды А, которые отдыхают. ',' '.join(players_a_rest) )
print('Все члены команды B, которые тренируются. ', ' '.join(players_b_trening ))
print('Все члены команды C, которые путешествуют. ',' '.join(players_c_travel))