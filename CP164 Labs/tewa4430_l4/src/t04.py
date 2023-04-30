'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-06"
-----------------------------------------------

'''
# Imports

# Constants
from List_array import List
lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
lst.append(6)
lst.append(7)
lst.append(8)
lst.append(9)
index_value = lst.index(6)
print("Index of 6 in the list is: {}".format(index_value))
find_value = lst.find(9)
print("Value found is {}".format(find_value))
check_value = lst.__contains__(5)
print("The list contains: {}".format(check_value))
max_value = lst.max()
print("Maximum value in the list is: {}".format(max_value))
min_value = lst.min()
print("Minimum value in the list is: {}".format(min_value))
