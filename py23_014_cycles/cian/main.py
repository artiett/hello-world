import csv
from pprint import pprint
flats_list = list()
with open('output.csv', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)
header = flats_list.pop(0)

# цикл с порядковыми номерами новостроек
count = 0
print('Новостройки:')
for i, flat in enumerate(flats_list):
    if "новостройка" in flat[2]:
        print("Квартира №{} с ID {}"
              .format(i+1, flat[0]))
        count += 1

# подсчет количества новостроек
print('Итого: {} новостройки\n\n'.format(count))


# описание квартиры в виде словаря
flat_info = {}
for flat in flats_list:
    flat_info = {'id': flat[0], 'rooms': flat[1],
                 'type': flat[2], 'price': flat[11]}
    print('В квартире с ID {} {} комнат. {}, стоит {}₽'
          .format(flat_info['id'], flat_info['rooms'],
                  flat_info['type'].capitalize(), flat_info['price']))

# квартиры, собранные по метро
subway_dict = {}
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
    subway_dict[subway].append({'id': flat[0],
                                'rooms': flat[1],
                                'type': flat[2],
                                'price': flat[11]})
pprint(subway_dict)


# подсчет квартир у каждого метро
for subway in subway_dict:
    print('У метро {} {} квартир'
          .format(subway, len(subway_dict[subway])))
