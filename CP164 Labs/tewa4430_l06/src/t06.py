'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-27"
-----------------------------------------------

'''
# Imports

# Constants
from List_linked import List
lst_link = List()
lst_link.append(1)
lst_link.append(2)
lst_link.append(3)
lst_link.append(4)
lst_link.append(5)
lst_link.append(1)
lst_link.append(1)
print("Linked List")
for i in lst_link:
    print(i)
print()
value = lst_link[2]
print("Value at index 2: {}".format(value))
print()
print("Changing the value at index 4")
lst_link[4] = 91
print("Linked list after changing value")
for j in lst_link:
    print(j)
