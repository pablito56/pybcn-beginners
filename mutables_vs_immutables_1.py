#-*- coding: utf-8 -*-
"pybcn mutables assignment bug example"


list1 = ["a", "b", "c"]
print "list1", list1, "@", id(list1)
print "-" * 5

list3 = list2 = list1
list2.append("x")
print "list1", list1, "@", id(list1)
print "list2", list2, "@", id(list2)
print "list3", list3, "@", id(list3)
print "-" * 5

mtrx1 = [[1, 1, 1], [2, 2, 2]]
print "mtrx1", mtrx1, "@", id(mtrx1)
print "-" * 5

mtrx2 = list(mtrx1)
mtrx2[0].append("a")
print "mtrx1", mtrx1, "@", id(mtrx1)
print "mtrx2", mtrx2, "@", id(mtrx2)
print "-" * 5
print "mtrx1[0]", mtrx1[0], "@", id(mtrx1[0])
print "mtrx2[0]", mtrx2[0], "@", id(mtrx2[0])
