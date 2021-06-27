"""
https://docs.python.org/3/library/  this path contain all the modules that exist in Python library
"""

import math  # basic way to import module, but if called this way it takes most of the memory while processing

from math import sqrt  # this was only those methods will be called from a module which are regarding in your code

# import modules_external.car as car  # another way to import method from a module but not recommended
from modules_external import car
# from modules_external.car import info


class ModulesDemo():
    def builtin_modules(self):
        print(math.sqrt(40))
        print(sqrt(100))

    def car_desc(self):
        make = "BMW"
        model = "550i"
        car.info(make, model)
        # info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car_desc()
