#-*- coding: utf-8 -*-
"pybcn class attributes bug example"

class ExampleClass(object):
    list_attr = []
    int_attr = 0

instA = ExampleClass()
instB = ExampleClass()

instA.int_attr += 1
instA.list_attr.extend([5, 7, 9])
print "instA.int_attr:", instA.int_attr
print "instA.list_attr:", instA.list_attr
print "-" * 5

print "instB.int_attr:", instB.int_attr
print "instB.list_attr:", instB.list_attr

print "-" * 5
print instA.list_attr is instB.list_attr
print ExampleClass.list_attr
