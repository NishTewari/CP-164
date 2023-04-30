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
print("list:")
for i in lst:
    print(i)
value = lst[2]
print("Value at index 2 is: {}".format(value))
lst[5] = 10
print("Value at index 5 is changed to")
print("Changed List:")
for j in lst:
    print(j)
