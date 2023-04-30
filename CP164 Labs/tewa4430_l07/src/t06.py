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
for num in [44, 55, 22, 11, 66, 33]:
    lst.append(num)
lst.reverse_r()
for nums in lst:
    print(nums)
