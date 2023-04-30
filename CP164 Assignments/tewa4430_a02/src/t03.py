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
from Food_utilities import calories_by_origin, read_foods

# Constants

fv = open("foods.txt")
foods = read_foods(fv)

origin = int(input("Enter a number for the food origin: "))
avg = calories_by_origin(foods, origin)

print("\nThe average calories for all foods in the specific origin is {}".format(avg))
