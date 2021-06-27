"""
Object Oriented Programming
"""

print("_____ CREATE YOUR OWN METHOD _____")


class Car(object):
    wheels = 4  # its the member variable, it can be used with the class and also with the instances.

    # but one should avoid using it with instances

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car is: " + self.make)
        print("Model of the car is: " + self.model)


c1 = Car('BMW', '550i')
c1.wheels = 5
print(c1.wheels)
# c1.info()

c2 = Car('BENZ', 'E250')
print(c2.wheels)
# c2.info()

print(Car.wheels)
