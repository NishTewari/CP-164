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
from Food_utilities import read_foods
from utilities import stack_test
# Constants

fv = open("foods.txt")
foods = read_foods(fv)
stack_test(foods)
