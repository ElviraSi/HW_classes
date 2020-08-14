class Animal:
    action = 'without action'
    voice = 'without'

    def __init__(self, nickname, weight=0):
        self.nickname = nickname
        self.weight = weight

    def feed(self):
        self.action = 'feed'
        print(f'I {self.action} {self.nickname}.')

    def __add__(self, weight):
        total_weight = 0
        total_weight += self.weight
        return total_weight

    def __gt__(self, other):
        return self.weight > other.weight


class Bird(Animal):
    def collect(self):
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


class Cow(Animal):
    def milk(self):
        self.action = 'milk'
        print(f'I {self.action} cow {self.nickname}.')

    def make_sounds(self):
        self.voice = 'moooooo'
        print(f'Cow {self.nickname} make sounds: {self.voice}.')


class Goat(Animal):
    def milk(self):
        self.action = 'milk'
        print(f'I {self.action} goat {self.nickname}.')

    def make_sounds(self):
        self.voice = 'baaaaa'
        print(f'Goat {self.nickname} make sounds: {self.voice}.')


class Sheep(Animal):
    def shear(self):
        self.action = 'shear'
        print(f'I {self.action} sheep {self.nickname}.')

    def make_sounds(self):
        self.voice = 'baaa'
        print(f'Sheep {self.nickname} make sounds: {self.voice}.')

#example
goat = Goat('Horns', 1000)
goat.milk()
goat.make_sounds()

chiken = Chiken('Co-Co', 120)
chiken.feed()
chiken.make_sounds()

print(goat + chiken)
print(goat > chiken)