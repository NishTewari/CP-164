'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-23"
-----------------------------------------------

'''
# Imports
from Food_utilities import food_table, read_foods
# Constants

fv = open("foods.txt")
foods = read_foods(fv)

food_table(foods)
