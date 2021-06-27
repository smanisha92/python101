"""Boolean Precedence
1. ()
2. not
3. and
4. or"""

bool_output = True or not False and False
print(bool_output)
bool_output1 = 10 == 10 or not 10 > 10 and 10 > 10
print(bool_output1)
bool_output2 = (10 == 10 or not 10 > 10) and 10 > 10
print(bool_output2)
