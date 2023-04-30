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
source = Stack()
source.push(12)
source.push(20)
source.push(12)
source.push(18)
source.push(5)
source.push(34)
source.push(4)
print("Source:")
for j in source:
    print(j)
    
target1, target2 = source.split_alt()
print("\nTarget1:")
for i in target1:
    print(i)

print("\nTarget2:")
for k in target2:
    print(k)
