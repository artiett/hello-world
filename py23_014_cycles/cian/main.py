import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)


#TODO 1:
count = 0
print('Новостройки:')
for i, flat in enumerate(flats_list):
  if "новостройка" in flat[2]:
    print("Квартира №{} с ID {}, стоит {} руб.".format(i+1, flat[0], flat[11]))
    count += 1
print('Итого: {} новостройки\n\n'.format(count))


#TODO 2:
flat_info = {"id": flat[0], "rooms": flat[1], "type": flat[2], "price": flat[11]}

subway_dict = {}
for flat in flats_list:
  subway = flat[3].replace("м.", "")
  if subway not in subway_dict.keys():
    subway_dict[subway] = list()
  subway_dict[subway].append(flat_info)
print(subway_dict)