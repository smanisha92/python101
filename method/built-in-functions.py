"""
Some built-in functions
max(): It takes any no. of arguments and returns the largest one.
min(): It takes any no. of arguments and returns the smallest one.
abs(): It returns the absolute value of the number, that number's distance from 0.
       It always returns a positive value and it only takes a single number.
type(): It returns the type of the data it receives as an argument.
"""
print("************* Learning max() function ********************")


def largest_num(*args):
    print(max(args))


largest_num(-20, -1, -10, -100)
print("**************Learning min() Function *******************")


def smallest_num(*args):
    print(min(args))


smallest_num(-20, -1, -10, -100)
print("************* Learning abs() function ********************")


def abs_num(a):
    print(abs(a))


abs_num(-30)
abs_num(40)
print("************* Learning type() function ********************")


print(type(99))
print(type(99.9))
print(type("abc"))
l = [1, 2, 2, 3, 5]
print(type(l))
d = {1: 2, 3: 4}
print(type(d))
t = (1, 2, 3, 4)
print(type(t))
