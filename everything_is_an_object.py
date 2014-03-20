#-*- coding: utf-8 -*-
"pybcn 'everything is an object' example"


def a_func(arg):
    "This is a function"
    return arg + arg


print a_func(2)

print a_func.func_doc

print a_func.func_name

print type(a_func), isinstance(a_func, object)
