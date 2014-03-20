#-*- coding: utf-8 -*-
"pybcn function default attribute bug example"

def add_power_to_list(item, powers_lst=[]):
    powers_lst.append(item ** 2)
    return powers_lst

print "default:", add_power_to_list.func_defaults
print "-" * 5

result1 = add_power_to_list(2)
print "result1:", result1
print "-" * 5

result2 = add_power_to_list(3)
print "result1:", result1, 'vs', "result2", result2
print result1 is result2
print "-" * 5

print "default:", add_power_to_list.func_defaults
