"""
variable scope
"""
a = 10


def test_method(a):
    print("value of local 'a' is: " + str(a))
    a = 2
    print("New Value of local 'a' is: " + str(a))


print("Value of global 'a' is: " + str(a))
test_method(a)
print("Did the value of 'a' global change? " + str(a))

print("****************************")
x = 10

#  to call global variable inside a method()


def test_methods():
    global x
    print("value of local 'x' is: " + str(x))
    a = 2
    print("New Value of local 'x' is: " + str(x))


print("Value of global 'x' is: " + str(x))
test_methods()
print("Did the value of 'x' global change? " + str(x))

