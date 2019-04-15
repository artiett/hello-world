#Приложение для финансового планирования

income=int(input('Введите заработную плату в месяц: '))
mortgage=int(input('Введите сколько процентов уходит на ипотеку: '))
liv_expenses=int(input('Введите сколько процентов уходит на жизнь: '))
extra_income=int(input('Введите количество премий за год: '))

print('Вывод:')
print('За год на ипотеку потрачено: ', int(income * 12
      * mortgage / 100), 'рублей')
print('За год накоплено: ', int(12 * income
      + extra_income * income / 2 - 12 * income
      * liv_expenses / 100 - income * 12
      * mortgage / 100), 'рублей')