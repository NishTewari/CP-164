'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-03-05"
-----------------------------------------------

'''
# Imports

# Constants
from List_linked import List
lst = List()
for num in [44, 33, 22, 66, 11, 55]:
    lst.append(num)
index, current, previous = lst._linear_search_r(66)
# print(previous._value)
print(current._value)
print(index)
