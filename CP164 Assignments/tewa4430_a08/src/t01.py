'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-03-26"
-----------------------------------------------

'''
from BST_linked import BST

# Constants
SEP = "-" * 30
BALANCED = [3, 1, 5, 0, 2, 4, 6]

bst = BST()

for v in BALANCED:
    bst.insert(v)

print("Values: {}".format(BALANCED))
print("\nPreorder")
print(bst.preorder())
print("\nInorder:")
print(bst.inorder())
print("\nPostorder")
print(bst.postorder())
print("\nLevelorder")
print(bst.levelorder())
print("\nMinimum")
print(bst.min())
print("\nLeaf Count")
print(bst.leaf_count())
print("\nOne Child Count")
print(bst.one_child_count())
print("\nTwo Child Count")
print(bst.two_child_count())
print("\nIs Balanced")
print(bst.is_balanced())
print("\nValid")
print(bst.is_valid())
