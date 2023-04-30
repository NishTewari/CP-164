'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-27"
-----------------------------------------------

'''
from List_linked import List
lst_link = List()
lst_link.append(1)
lst_link.append(2)
lst_link.append(3)
lst_link.append(4)
lst_link.append(1)
lst_link.append(1)
number = lst_link.count(1)
print("The number of times 1 appear is: {}".format(number))
max = lst_link.max()
print("The maximum number is: {}".format(max))
min = lst_link.min()
print("The minimum number is: {}".format(min))
