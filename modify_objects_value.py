#-*- coding: utf-8 -*-
"pybcn modify objects value example"


txt1 = "This is text"
print id(txt1), txt1

txt2 = txt1 + " and more text"  # Which object is txt2?
print id(txt2), txt2
print "-" * 5

int1 = 7
print id(int1), int1

int1 += 11  # Which object is int1?
print id(int1), int1
print "-" * 5

list1 = ["a", "b", "c"]
print id(list1), list1

list1.extend([0, 1, 2])  # In place modification
list1[0] = "XXX"
print id(list1), list1
