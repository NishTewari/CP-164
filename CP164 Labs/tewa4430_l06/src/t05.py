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
lst_link.append(6)
lst_link.append(1)
lst_link.append(1)
print("Linked List")
for i in lst_link:
    print(i)
print()
value = lst_link.peek()
print("The value at the front of the list: {}".format(value))
lst_link.remove(3)
print("Value 3 is removed from the list")
print("List after removing a value")
for j in lst_link:
    print(j)
