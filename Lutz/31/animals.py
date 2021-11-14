class Animal:
    def reply(self):
        return self.speak()


class Mammal(Animal):
    def speak(self):
        return '*sound*'


class Cat(Mammal):
    def speak(self):
        return 'Meow'


class Dog(Mammal):
    def speak(self):
        return 'Whoof-whoof'


class Primate(Mammal):
    def speak(self):
        return 'Уу-аа'


class Hacker(Primate):
    def speak(self):
        return 'Ща взломаю'


spot = Cat()
print(spot.reply())
data = Hacker()
print(data.reply())