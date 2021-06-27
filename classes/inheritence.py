"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class. Child class is the class that inherits
from another class, also called derived class.
"""


class Car(object):
    def __init__(self):
        print("I just created a parent car company")

    def drive(self):
        print("You can test drive all the car in this company")

    def stop(self):
        print("You can park the car once test drove")


c = Car()
c.drive()
c.stop()

print("*****************************************************************")


class Bmw(Car):
    def __init__(self):
        Car.__init__(self)
        print("First car in this company is BMW")


b = Bmw()
b.drive()
b.stop()


print("******_____ Lets learn Method Overriding _____******")


class Cars(object):
    def __init__(self):
        print("I just created a parent car company")

    def drive1(self):
        print("You can test drive all the car in this company, Go ahead start driving...")

    def stop1(self):
        print("You can park the car once test drove")


c = Cars()
c.drive1()
c.stop1()

print("*****************************************************************")


class BMW(Cars):
    def __init__(self):
        Cars.__init__(self)
        print("First car in this company is BMW")

    def drive1(self):  # Method Overriding: you can create method with same name as of parent class in your child class
        super(BMW, self).drive1()
        print("You are driving a brand new BMW. Enjoy!!!!!!")


b = BMW()
b.drive1()
b.stop1()
