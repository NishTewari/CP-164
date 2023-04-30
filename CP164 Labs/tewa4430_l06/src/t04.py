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
lst_link.append(6)
lst_link.append(2)
lst_link.append(3)
lst_link.append(4)
lst_link.append(1)
lst_link.append(1)
value = lst_link.find(3)
print(value)
index = lst_link.index(1)
print("The index of 1 is: {}".format(index))
contains = 5 in lst_link
print("Is 5 in the list: {}".format(contains))
