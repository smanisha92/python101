"""
Exercise
Create a class Fruit
Define 3 methods in this class
__init__()
nutrition()
fruit_shape()

Print anything you like in these methods

CReate one more class (Any Fruit Name)
This class should inherit from the Fruit Class created above, this will become the child class and "Fruit"
will be referred as parent class to this class

Define 3 Methods in this class
__init__()
nutrition()
color()

Print anything you like in these methods

Create instances of these classes and call methods from them
Call methods from the base class also using the instance of the child class

"""


class Fruit(object):
    def __init__(self):
        print("Lets buy some fruits and learn about them")

    def nutrition(self):
        print("Fruits are very nutritious for your health")

    def fruit_shape(self):
        print("What all shape fruit is available in the market")


class Guava(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("I am Guava")

    def nutrition(self):
        super(Guava, self).nutrition()
        print("I have so many health benefits and am super nutritious")

    def color(self):
        print("I am green in color")


f = Fruit()
f.nutrition()
f.fruit_shape()

print("**********************************")

g = Guava()
g.fruit_shape()
g.nutrition()
g.color()

