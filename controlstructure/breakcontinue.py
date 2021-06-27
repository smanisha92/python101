"""
Break: To break out of the closest enclosing loops
Continue: Go to the start of the closest enclosing loop
"""
x = 0
while x < 5:
    print("value of x is: " + str(x))
    x = x + 1
    if x == 8:
        break
    print("Learnt Break Logic")
    print("*" * 20)
print("Just broke out of the loop")
print("_______ LEARNING CONTINUE LOGIC _______")
x = 0
while x < 5:
    print("value of x is: " + str(x))
    x = x + 1
    if x == 8:
        continue
    print("Learnt Continue Logic")
    print("*" * 20)
print("Just came out of the loop")
print("______ LEARNING WHILE ELSE LOGIC ______")
x = 0
while x < 5:
    print("value of x is: " + str(x))
    x = x + 1
    print("Learning Python Coding")
    print("*" * 20)
else:
    print("Just broke out of the loop")
print("______ LEARNING WHILE ELSE WITH BREAK LOGIC ______")
x = 0
while x < 5:
    print("value of x is: " + str(x))
    x = x + 1
    if x == 3:
        break
    print("Learning Python Coding")
    print("*" * 20)
else:
    print("Just broke out of the loop")
