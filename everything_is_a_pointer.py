#-*- coding: utf-8 -*-
"pybcn 'everything is a pointer' example"

class MyClass(object):
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

def print_id_and_return(attr):
    print "Attr id:", id(attr)
    return attr

inst = MyClass(3, 4)

print "Instance:", id(inst)

ret_val = print_id_and_return(inst)

print inst is ret_val
