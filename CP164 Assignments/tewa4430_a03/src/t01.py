'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-30"
-----------------------------------------------

'''
# Imports

# Constants
from Stack_array import Stack
from functions import stack_split_alt

source = Stack()
source.push(5)
source.push(9)
source.push(18)
source.push(9)
source.push(10)
source.push(7)
source.push(6)
print("Source:")
for k in source:
    print(k)
target1, target2 = stack_split_alt(source)
print("\nTarget1:")
for i in target1:
    print(i)
print("\nTarget2:")
for j in target2:
    print(j)

