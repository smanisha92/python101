"""
Positional Parameters
They are like optional parameters
and can be assigned a default value, if no value is provided from outside
"""


def sum_num(n1=5, n2=9):
    """
    Learning return function in Method()
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_num(n2=12)
print(sum1)

