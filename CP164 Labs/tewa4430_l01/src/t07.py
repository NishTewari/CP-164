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
from Food_utilities import get_vegetarian, read_foods
# Constants
from t05 import file_variable

foods = read_foods(file_variable)

veggies = get_vegetarian(foods)
print(veggies)
