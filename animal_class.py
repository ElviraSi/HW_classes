class Animal:
    action = 'without action'
    voice = 'without'

    def __init__(self, nickname, weight=0):
        self.nickname = nickname
        self.weight = weight

    def feed(self):
        self.action = 'feed'
        print(f'I {self.action} {self.nickname}.')

    #дополнительная возможность сравнить вес двух животных
    def __gt__(self, other):
        return self.weight > other.weight


class Bird(Animal):
    def collect_eggs(self):
        self.action = 'collect eggs'
        print(f'I {self.action} {self.nickname}.')


class Goose(Bird):
    def make_sounds(self):
        self.voice = 'honk-honk'
        print(f'Goose {self.nickname} make sounds: {self.voice}.')


class Duck(Bird):
    def make_sounds(self):
        self.voice = 'quack-quack'
        print(f'Duck {self.nickname} make sounds: {self.voice}.')


class Chiken(Bird):
    def make_sounds(self):
        self.voice = 'cluck-cluck'
        print(f'Chiken {self.nickname} make sounds: {self.voice}.')


class Cattle(Animal):
    def get_milk(self):
        self.action = 'get milk'
        print(f'I {self.action} cow {self.nickname}.')


class Cow(Cattle):
    def make_sounds(self):
        self.voice = 'moooooo'
        print(f'Cow {self.nickname} make sounds: {self.voice}.')


class Goat(Cattle):
    def make_sounds(self):
        self.voice = 'baaaaa'
        print(f'Goat {self.nickname} make sounds: {self.voice}.')


class Sheep(Animal):
    def get_wool(self):
        self.action = 'shear'
        print(f'I {self.action} sheep {self.nickname}.')

    def make_sounds(self):
        self.voice = 'baaa'
        print(f'Sheep {self.nickname} make sounds: {self.voice}.')

#создание списка с экземплярами класса
Animal = []
Animal.append(Goose('Серый', 10))
Animal.append(Goose('Белый', 7))
Animal.append(Cow('Манька', 150))
Animal.append(Sheep('Барашек', 48))
Animal.append(Sheep('Кудрявый', 52))
Animal.append(Chiken('Ко-Ко', 2))
Animal.append(Chiken('Кукареку', 1))
Animal.append(Goat('Рога', 34))
Animal.append(Goat('Копыта', 28))
Animal.append(Duck('Кряква', 4))

#расчет общего веса всех животных
weight_list = [cl.weight for cl in Animal]
total_weight = 0
for i in weight_list:
    total_weight += i
print(f'Общий вес всех животных составляет: {total_weight} кг.')

#нахождение животного с максимальным весом
animal_list = [cl.nickname for cl in Animal]
animal_dict = dict(zip(animal_list, weight_list))
max_weight = max(animal_dict, key=animal_dict.get)
print(f'Максимальный вес имеет {max_weight}.')