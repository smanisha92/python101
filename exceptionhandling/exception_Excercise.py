"""
Create a dictionary "car"
create 3 keys
- make
- model
- year

try to access the color key. remember we never created a color key, so its going to throw an exception.
YOu need to handle the execution using try, except and finally block
"""


def exceptionHandling():
    try:
        d = {'make': "BMW", 'model': "550i", 'year': 2020}
        print(d['color'])
    except:
        print("This is an exception")
    finally:
        print("Finally will always print")


exceptionHandling()
