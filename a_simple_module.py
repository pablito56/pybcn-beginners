#-*- coding: utf-8 -*-
"pybcn basic module example"  # Module docstring

from random import randint  # An import


class MyClass(object):  # A class declaration
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


def random_instance():  # A function declaration
    "Create an instance of MyClass with random values"
    attr1_val = randint(0, 10)
    attr2_val = randint(0, 10)
    return MyClass(attr1_val, attr2_val)


# We execute some statements
inst = random_instance()
print "Instance:", inst, inst.attr1, inst.attr2
