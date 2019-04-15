# Пример использования библиотек
watchlist = {
  'Dr. No': True,
  'From Russia with Love': True,
  'Goldfinger': True,
  'Thunderball': False,
  'You Only Live Twice': True,
  'On Her Majesty’s Secret Service': True,
  'Diamonds Are Forever': True,
  'Live and Let Die': True,
  'The Man with the Golden Gun': True,
  'The Spy Who Loved Me': True,
  'Moonraker': True,
  'For Your Eyes Only': True,
  'Octopussy': False,
  'A View to a Kill': True,
  'The Living Daylights': True,
  'Licence to Kill': True,
  'GoldenEye': True,
  'Tomorrow Never Dies': True,
  'The World Is Not Enough': True,
  'Die Another Day': True,
  'Casino Royale': False,
  'Quantum of Solace': False,
  'Skyfall': False,
  'Spectre': False
}
print('Нужно посмотреть:')
for film, viewed in watchlist.items():
  if viewed == False:
    print(film)

# Пример использования списков и кортежей
eclipse_1935 = [
  1935,
  [('янв'), (5)],
  [('фев'), (3)],
  [('июн'), (30)],
  [('июл'), (30)], 
  [('дек'), (25)]
]
year = eclipse_1935.pop(0)
print('\n')
for i, date in enumerate(eclipse_1935):
  print('{} {} было {} затмение из {} случившихся в {} году'.format(date[1], date[0], i+1, len(eclipse_1935), year))

# Пример использования множеств
my_vinyls = ("Ecstasy", "Transformer", "Berlin", "Street Hassle", "Growing Up in Public")
store = ("Transformer", "Growing Up in Public", "Ecstasy", "Sally Can't Dance")
print('\n\nВ коллекцию можно добавить {}'.format(set(store).difference(set(my_vinyls))))