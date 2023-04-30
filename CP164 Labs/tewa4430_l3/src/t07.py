'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-30"
-----------------------------------------------

'''
# Imports
from Food_utilities import read_foods
from utilities import priority_queue_test
fv = open("foods.txt")
foods = read_foods(fv)

priority_queue_test(foods)  
