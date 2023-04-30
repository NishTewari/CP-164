'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-04-02"
-----------------------------------------------

'''
# Imports
from BST_linked import BST

# Constants
SEP = '-' * 60
BALANCED = [11, 7, 15, 6, 9, 12, 18, 8]

bst = BST()

for v in BALANCED:
    bst.insert(v)

data = bst.preorder()
print("BST data preorder: {}".format(data))
print(SEP)
key = 999
print("Attempt to remove invalid key: {}".format(key))
r = bst.remove(key)
print("Value removed: {}".format(r))
data = bst.preorder()
print("BST data preorder: {}".format(data))
print(SEP)
print("Remove node with one child: 9")
r = bst.remove(9)
print("Value removed: {}".format(r))
data = bst.preorder()
print("BST data preorder: {}".format(data))
print(SEP)
print("Remove node with no child: 12")
r = bst.remove(12)
print("Value removed: {}".format(r))
data = bst.preorder()
print("BST data preorder: {}".format(data))
print(SEP)
print("Remove node with two children: 11")
r = bst.remove(11)
print("Value removed: {}".format(r))
data = bst.preorder()
print("BST data preorder: {}".format(data))
print(SEP)
