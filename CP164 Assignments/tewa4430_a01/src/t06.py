'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-15"
-----------------------------------------------

'''
# Imports
from functions import matrixes_multiply
# Constants

a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

c = matrixes_multiply(a, b)

for z in c:
    print(z)
