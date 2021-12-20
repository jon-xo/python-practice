#!/usr/bin/env python

global_variable = 'global'

print(' -- Local and global Namespaces with empty script -- \n')

print(locals())
print(globals())


def divide(num1, num2):
    result = num1 / num2
    print(locals())

def multiply(num1, num2):
    product = num1 * num2
    print(locals())



print(' -- Local Namespaces for divide -- \n')

divide(3, 4)


print(' -- Local Namespaces for multiply -- \n')
multiply(4, 50)