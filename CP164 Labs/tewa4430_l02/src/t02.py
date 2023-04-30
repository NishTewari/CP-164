'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-21"
-----------------------------------------------

'''
# Imports
from Stack_array import Stack
from utilities import array_to_stack

source = [11, 22, 33, 44, 55, 66]
stack = Stack()
array_to_stack(stack, source)

print("List: {}".format(source))
print("Stack:")
for i in stack:
    print(i)

