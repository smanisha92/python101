"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

name = input("What is your name: ")
age = int(input("What is your age: "))
this_year = int(input("Which year is this: "))
year = str((this_year - age) + 100)
print(name + " will be 100 year old in the year " + year)
