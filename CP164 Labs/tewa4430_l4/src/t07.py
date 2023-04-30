'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-06"
-----------------------------------------------

'''
from Food_utilities import read_foods
from List_array import List
from utilities import list_test

fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
    
list_test(foods)

fv.close()
