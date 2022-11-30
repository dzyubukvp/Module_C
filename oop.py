
a = int(5)
s = str('5')
print(type(a))
print(type(s))

class Car:
    def __init__(self, name, model, color, **kwargs):
        self.name = name
        self.model = model
        self.color = color
        if 'hp' in kwargs:
            self.hp = kwargs['hp']
        else:
            self.hp = 86

    def tunning(self, power):
        self.hp += power

    def info(self):
        print('My', self.name, self.model, 'has', self.hp, 'HP', 'the car is', self.color )



audi = Car('Audi', 'a4', 'red')
bmw = Car('BMW', '3201', 'Wite')
lada = Car('ЖИГУЛИ', 'VAZ2108', 'green')
bmw.tunning(101)
audi.tunning(9)
print(audi.hp)

print(lada.hp)
print(bmw.hp)

audi.info()
bmw.info()
lada.info()