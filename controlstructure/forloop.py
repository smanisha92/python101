"""
For Loop Session
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are strings. list. Tuple, Dictionary
"""
print("____ FOR LOOP IN STRINGS ____")
my_string = 'abcabc'
for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')
print()
print("____ FOR IN LIST ____")
cars = ['BMW','AUDI','BENZ']
for car in cars:
    print(car)
num = [1,2,3]
for n in num:
    print(n * 5)
print("____ FOR IN TUPLE ____")
num = (1,2,3)
for n in num:
    print(n * 10)
print("____ FOR IN DICYIONARY ____")
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k + " " + str(d[k]))

for k,v in d.items():
    print(k)
    print(v)
