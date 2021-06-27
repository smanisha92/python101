"""
Exceptions are errors
We should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exceptions - https://docs.python.org/3/library/exceptions.html
"""


def exceptionHandling():
    try:
        a = 10
        b = "string"
        c = 0
        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("Zero Division Error")
    except TypeError:
        print("String cannot be added to Integer")


exceptionHandling()

print("+++++____ Learn Finally and Else Block ____+++++")


def exceptionHandle():
    try:
        a = 10
        b = 20
        c = 10
        d = (a + b) / c
        print(d)
    except:
        print("This is an exception")
        raise Exception("This cannot be processed")
    else:
        print("Because there is no exception, it printed")
    finally:
        print("Finally is always printed")


exceptionHandle()
