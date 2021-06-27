"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it
and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than
that number given by the user.
"""
print("___________ Numbers less than 5 in a list __________")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if num < 5:
        print(num)
    else:
        pass

#  print([aa for aa in a if aa < 5])

print("___________ Numbers divisible by 5 in a list __________")
x = [1, 10, 20, 22, 12, 23, 30, 16, 15, 21, 5]
for num1 in x:
    if num1 % 5 == 0:
        print(num1, end="\t")
    else:
        pass
