# Дейтинг клиент

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()
couples = zip(boys, girls)
not_enough = 'Not enough partners to couple all participants. Add another one'

if len(boys) == len(girls):
  print('Perfect matches: ')
  for boy, girl in couples:
    print(boy, 'and', girl)
else:
  print(not_enough)