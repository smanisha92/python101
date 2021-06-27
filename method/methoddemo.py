def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    print(n1 + n2)


sum_nums(3, 8)
y = [1, 2, 3]
print(y.append(5))
print(y)
print(len(y))
"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""


def sum_num(n1, n2):
    """
    Learning return function in Method()
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_num(2, 8)
print(sum1)
sum2 = sum_num(3, 18)
print(sum2)


def isMetro(city):
    x = ['noida', 'jaipur', 'delhi', 'agra', 'gurgaon', 'allahabad', 'varanasi']
    if city in x:
        return True
    else:
        return False


call_city = isMetro('agra')
print(call_city)
