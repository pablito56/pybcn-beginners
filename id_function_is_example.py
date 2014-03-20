#-*- coding: utf-8 -*-
"pybcn 'id' function and 'is' example"

class MyClass(object):
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

inst1 = MyClass(1, 1)
inst2 = MyClass(2, 2)
inst3 = inst1  # Copy?

# 'id' function returns the unique identity of an object
print "Instance 1:", id(inst1), inst1.attr1, inst1.attr2
print "Instance 2:", id(inst2), inst2.attr1, inst2.attr2
print "Instance 3:", id(inst3), inst3.attr1, inst3.attr2
print inst1 is inst3  # 'is' compares the identity
