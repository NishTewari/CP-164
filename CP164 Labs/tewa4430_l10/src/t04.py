'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-04-02"
-----------------------------------------------

'''
# Imports

# Constants

from test_Sorts_List_linked import test_sort, SORTS
print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")
for i in SORTS:
    title = i[0]
    func = i[1]
    test_sort(title, func)
