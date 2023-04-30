'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-03-26"
-----------------------------------------------

'''
# Imports
from BST_linked import BST
from Letter import Letter
from functions import letter_table, do_comparisons, DATA3

# initiate a BST
FILE = "miserables.txt"

pop_bst = BST()

# fill them with letter objects
for i in range(len(DATA3)):
    pop_bst.insert(Letter(DATA3[i]))

fv = open(FILE, "r", encoding="UTF-8")
do_comparisons(fv, pop_bst)
fv.close()  
letter_table(pop_bst)
