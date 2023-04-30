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
from Food_utilities import food_search, read_foods
# Constants

fv = open("foods.txt")
foods = read_foods(fv)

origin = int(input("Enter a number for the food origin: "))
max_cals = int(input("Enter the maximum number of calories: "))
is_veg = input("Enter (T) for vegetarian food and (F) for Non-veg food: ")
result = food_search(foods, origin, max_cals, is_veg)
print()
print(result)
