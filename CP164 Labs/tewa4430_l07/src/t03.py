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
for num in [11, 22, 33, 44, 55, 66]:
    lst.append(num)
target1, target2 = lst.split_alt_r()
for nums in target1:
    print(nums)
print()
print(len(target1))
print(len(lst))
