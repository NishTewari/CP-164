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

from List_array import List
from utilities import array_to_list, list_to_array
llist = List()
source = [11, 22, 33, 44, 55]
array_to_list(llist, source)
for i in llist:
    print(i)
target = []
list_to_array(llist, target)
print(target)
