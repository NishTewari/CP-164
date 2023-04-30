'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-03-05"
-----------------------------------------------

'''
from List_linked import List
lst = List()
for num in [44, 33, 22, 66, 11, 55]:
    lst.append(num)
lst2 = List()
for num in [44, 22, 11, 11, 11, 1, 2, 3]:
    lst2.append(num)
lst3 = List()
lst3.union_r(lst, lst2)
for num in lst3:
    print(num)
