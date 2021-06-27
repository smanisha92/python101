"""
Iterating multiple lists at the same time
"""
l1 = [1,2,3]
l2 = [6,7,8,10,20,30]
for a,b in zip(l1, l2):
    if (a < b):
        print(a)
    else:
        print(b)

print("____ LEARNING RANGE BUILT IN FUNCTION ____")
"""
Built in function
Creates a sequence of numbers but does not save them in memory
very useful for generating numbers"""
print(list(range(0,10)))
a = range(0,15,3)
print(a)
print(type(a))
print(list(a))
l = [1,2,3]
for num in l:
    print(num)
for num in range(1,4,2):
    print(num)