'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-30"
-----------------------------------------------

'''
from Food_utilities import read_foods
from utilities import queue_test
fv = open("foods.txt")
foods = read_foods(fv)
queue_test(foods)
