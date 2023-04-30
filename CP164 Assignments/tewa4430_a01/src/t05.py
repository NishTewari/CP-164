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
from functions import matrixes_add
# Constants

a = [[0, 1], [2, 3], [4, 5]]

b = [[6, 7], [8, 9], [1, 0]]

c = matrixes_add(a, b)

for z in c:
    print(z)
