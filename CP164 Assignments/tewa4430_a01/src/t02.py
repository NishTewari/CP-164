'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-13"
-----------------------------------------------

'''
# Imports
from functions import is_valid
# Constants
    
name = input("Enter a Valid Python Variable Name: ")

valid = is_valid(name)  

print("{} : {}".format(name, valid))
