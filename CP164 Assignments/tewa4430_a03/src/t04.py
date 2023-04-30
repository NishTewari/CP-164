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

from Stack_array import Stack
target = Stack()
source1 = Stack()
source1.push(12)
source1.push(50)
source1.push(13)
source1.push(67)
source2 = Stack()
source2.push(78)
source2.push(59)
source2.push(7)
source2.push(13)
source2.push(62)
source2.push(31)

print("Source1:")
for j in source1:
    print(j)

print("\nSource2:")
for k in source2:
    print(k)

target.combine(source1, source2)
print("\nTarget:")
for i in target:
    print(i)
