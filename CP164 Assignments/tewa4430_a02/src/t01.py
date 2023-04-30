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
from Food_utilities import by_origin, read_foods

fv = open("foods.txt")
foods = read_foods(fv)
origin = int(input("Enter a number for the food origin: "))
origins = by_origin(foods, origin)

print()
print(origins, "\n")
for i in origins:
    print(str(i))
    print()
