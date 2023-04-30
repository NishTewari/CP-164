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
from Food_utilities import write_foods, read_foods
# Constants
from t05 import file_variable

file_variable = open("foods.txt", "r")
file_var2 = open("new_foods.txt", "w")

foods = read_foods(file_variable)

write_foods(file_var2, foods)

file_variable.close()
file_var2.close()

