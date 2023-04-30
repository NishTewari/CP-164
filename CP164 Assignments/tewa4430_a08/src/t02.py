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
from functions import do_comparisons, comparison_total, DATA1, DATA2, DATA3

# Constants
SEP = "-" * 30
FILE = "miserables.txt"

# initiate 3 BSTs
order_bst = BST()
split_bst = BST()
popular_bst = BST()

# fill them with letter objects
for i in range(len(DATA1)):
    order_bst.insert(Letter(DATA1[i]))
    split_bst.insert(Letter(DATA2[i]))
    popular_bst.insert(Letter(DATA3[i]))

# open file
fv = open(FILE, "r", encoding="UTF-8")

do_comparisons(fv, order_bst)
order_com = comparison_total(order_bst)
do_comparisons(fv, split_bst)
split_com = comparison_total(split_bst)
do_comparisons(fv, popular_bst)
pop_com = comparison_total(popular_bst)

fv.close()

print("For '{}':".format(FILE))
print("\nComparing by order: {}".format(DATA1))
print("Total Comparisons: {:,}".format(order_com))
print(SEP)
print("Comparing by order: {}".format(DATA2))
print("Total Comparisons: {:,}".format(split_com))
print(SEP)
print("Comparing by order: {}".format(DATA3))
print("Total Comparisons: {:,}".format(pop_com))

