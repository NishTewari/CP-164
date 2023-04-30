'''
-----------------------------------------------
Functions for Question 2 and 3 
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-03-26"
-----------------------------------------------

'''
# Imports
from Letter import Letter

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    
    file_variable.seek(0)

    for line in file_variable:

        for char in line.strip():

            if char.isalpha():
                l = Letter(char.upper())
                bst.retrieve(l)
    return


# Constants
def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    a = bst.inorder()

    for var in a:
        total = total + var.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    t = 0
    a = bst.inorder()

    for i in a:
        t += i.count
    print("Letter Count/Percent Table\n")
    print("Total Count: {:,}".format(t))
    print("\nLetter  Count          %")
    print("------------------------")
    for i in a:
        print("{:>2}{:9,d}{:>13.2%}".format(i.letter, i.count, i.count / t))
    return
