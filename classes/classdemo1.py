"""
Object Oriented Programming
"""


class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model


c1 = Car('BMW', '550i')
print(c1.make)
print(c1.model)

c2 = Car('BENZ', 'E250')
print(c2.make)
print(c2.model)

print("******************************************************")


class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car is: " + self.make)
        print("Model of the car is: " + self.model)


c1 = Car('BMW', '550i')
c1.info()

c2 = Car('BENZ', 'E250')
c2.info()