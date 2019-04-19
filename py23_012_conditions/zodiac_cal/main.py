# зодиакальный календарь

month = input('Введите месяц: ')
date = int(input('Введите день: '))

if month == ('март' or 'Март'):
  if date < 21:
    print('рыбы')
  else:
    print('овен')

elif month == ('апрель' or 'Апрель'):
  if date < 19:
    print('овен')
  else:
    print('телец')

elif month == ('май' or 'Май'):
  if date < 21:
    print('телец')
  else:
    print('близнецы')

elif month == ('июнь' or 'Июнь'):
  if date < 21:
    print('близнецы')
  else:
    print('рак')

elif month == ('июль' or 'Июль'):
  if date < 23:
    print('рак')
  else:
    print('лев')

elif month == ('август' or 'Август'):
  if date < 22:
    print('лев')
  else:
    print('дева')

elif month == ('сентябрь' or 'Сентябрь'):
  if date < 22:
    print('дева')
  else:
    print('весы')

elif month == ('октябрь' or 'Октябрь'):
  if date < 22:
    print('весы')
  else:
    print('скорпион')

elif month == ('ноябрь' or 'Ноябрь'):
  if date < 21:
    print('скорпион')
  else:
    print('стрелец')

elif month == ('декабрь' or 'Декабрь'):
  if date < 21:
    print('стрелец')
  else:
    print('козерог')

elif month == ('январь' or 'Январь'):
  if date < 19:
    print('козерог')
  else:
    print('водолей')

elif month == ('февраль' or 'Февраль'):
  if date < 18:
    print('водолей')
  else:
    print('рыбы')

else:
  print('Попробуйте ещё раз')