"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
print("_______ Number is Even or Odd _______")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number entered by you is an even number")
else:
    print("Number entered by you is an odd number")

print("_______Code for part 1 _______")

num1 = int(input("Enter a number: "))
if num1 % 4 == 0:
    print(num1, "is divisible by 4")
elif num1 % 2 == 0:
    print("Number entered by you is an even number")
else:
    print("Number entered by you is an odd number")

print("_______Code for part 2 _______")

num2 = int(input("Enter a number: "))
check = int(input("Give me a number to be divide by: "))

if num2 % check == 0:
    print(num2, "divides evenly by", check)
else:
    print(num2, "does not divides evenly by", check)
