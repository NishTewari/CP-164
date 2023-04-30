'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-16"
-----------------------------------------------

'''
# Imports
from functions import matrix_stats
# Constants

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

small, large, total, average = matrix_stats(a)

print("Small: {:.1f}\n".format(small))
print("Large: {:.1f}\n".format(large))
print("Total: {:.1f}\n".format(total))
print("Average: {:.1f}\n".format(average))
