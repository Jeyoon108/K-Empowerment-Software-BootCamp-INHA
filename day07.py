# class - 교재

class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    # pass
    def says(self):
        return '말!'


class Donkey(Animal):
    # pass
    def says(self):
        return '당나귀!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


m1 = Mule()
print(m1.says())
h1 = Hinny()
print(h1.says())

print(Mule.mro())