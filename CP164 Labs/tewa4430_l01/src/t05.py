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
from Food_utilities import read_foods
# Constants

file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)

for i in foods:
    print(i)
    print("")
