"""
a = "nyc"
b = "nyc"
print(a)
a = 123
print(a)
print(b)
b = 456
print(b)
c = "nyc"
d = c
print(d == c)
print(d is c)
"""
import keyword
print(keyword.kwlist)
a = b = c = 100
print(a)
print(b+c)
print(a+(a*b)+c)
x, y, z = 10, 20, 30
print(y)
print(x*y+z-x)
print(y*z+(x-1))
