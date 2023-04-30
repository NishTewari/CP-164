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
for num in [55, 33, 66, 44, 22, 11]:
    lst2.append(num)
print(lst.is_identical(lst2))
lst3 = List()
lst4 = List()
for num in [55, 33, 66, 44, 22, 11]:
    lst3.append(num)
    lst4.append(num)
print(lst3.is_identical(lst4))
