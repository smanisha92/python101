print("*********** BOOLEAN OPERATORS EXAMPLES ************")
"""
and 
***************************
TRUE and TRUE -> TRUE
TRUE and FALSE -> FALSE
FALSE and FALSE -> FALSE
***************************
or 
***************************
TRUE or TRUE -> TRUE
TRUE or FALSE -> TRUE
FALSE or FALSE -> FALSE
***************************
not
***************************
NOT TRUE -> FALSE
NOT FALSE -> TRUE
"""
print("**** AND OPERATOR ****")
and_operator = (10 == 10) and (10 >= 10)
print(and_operator)
and_operator = (10 == 10) and (10 > 10)
print(and_operator)
and_operator = (10 != 10) and (10 > 10)
print(and_operator)

print("**** OR OPERATOR ****")
or_operator = (10 == 10) or (10 >= 10)
print(or_operator)
or_operator = (10 == 10) or (10 > 10)
print(or_operator)
or_operator = (10 != 10) or (10 > 10)
print(or_operator)

print("**** NOT OPERATOR ****")
not_operator = not(10 == 11)
print(not_operator)
not_operator = not(10 == 10)
print(not_operator)
