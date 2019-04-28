class DomesticAnimals:
    weight_sum = 0
    hungry = True
    def __init__(self, weight, feet, color, name):
        self.weight = weight
        self.feet = feet
        self.color = color
        self.name = name
        DomesticAnimals.weight_sum += weight
    def voice(self, call):
        print(call)
    def hunger(self):
        if self.hungry:
            print('Животное нужно покормить')
        else:
            print('Животное сыто')
    def feed(self):
        if self.hungry:
            print('Кормим животное')
            self.hungry = False
            return self.hungry
        else:
            print('Уже кормили это животное')

    # farm_weight = 0
    # for weight in self.weight:
    #     farm_weight += weight[0]

class Birds(DomesticAnimals):
    wings = True
    eggs = True
    def get_eggs(self):
        if self.eggs:
            print('Собираем яйца')
            self.eggs = False
            return self.eggs
        else:
            print('Яиц пока нет')
class Natatorials(Birds):
    swimming = True
class Ducks(Natatorials):
    def voice(self, call = '*вопросительно крякает*'):
        super(Ducks, self).voice(call)
class Hens(Birds):
    def voice(self, call = '*возмущённо кудашчет*'):
        super(Hens, self).voice(call)
class Geese(Natatorials):
    def voice(self, call = '*истошно верещит*'):
        super(Geese, self).voice(call)
class Ungulates(DomesticAnimals):
    horns = True
class Milch(Ungulates):
    milk = True
    def get_milk(self):
        if self.milk:
            print('Нужно подоить')
            self.milk = False
            return self.milk
        else:
            print('Уже подоили, пока не нужно')
class Cows(Milch):
    def voice(self, call = '*аппатично мычит*'):
        super(Cows, self).voice(call)
class Goats(Milch):
    def voice(self, call = 'Я так устал'):
        super(Goats, self).voice(call)
class Sheep(Ungulates):
    def voice(self, call = '*протяжно блеет*'):
        super(Sheep, self).voice(call)
    wool = True
    def shear(self):
        if self.wool:
            print('Пора стричь')
            self.wool = False
            return self.wool
        else:
            print('Уже постригли, пока не отросло')

goose_1 = Geese(4.1, 2, 'grey', 'Серый')
goose_2 = Geese(5.3, 2, 'white', 'Белый')
cow = Cows(210.4, 4, 'motley', 'Манька')
sheep_1 = Sheep(70.3, 4, 'white', 'Барашек')
sheep_2 = Sheep(71.1, 4, 'white', 'Кудрявый')
hen_1 = Hens(1.7, 2, 'motley', 'Ко-Ко')
hen_2 = Hens(1.7, 2, 'black', 'Кукареку')
goat_1 = Goats(30.1, 4, 'white', 'Рога')
goat_2 = Goats(26.0, 4, 'white', 'Копыта')
duck = Ducks(7.4, 2, 'white', 'Кряква')

print('Дядюшка Джо:\n -А ты знаешь, племяшек, сколько всё'
      ' моё хозяйство весит? {} кило! Тяжелее всех {}'
      .format(DomesticAnimals.weight_sum, cow))