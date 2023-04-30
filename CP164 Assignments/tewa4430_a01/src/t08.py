'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-16"
-----------------------------------------------

'''
# Imports
from functions import file_analyze
# Constants

fv = open("randomtext.txt", "r")

u, l, d, w, r = file_analyze(fv)

print("Number of uppercase letters within the file: {}".format(u))
print("Number of lowercase letters within the file: {}".format(l))
print("Number of digits within the file: {}".format(d))
print("Number of whitespace within the file: {}".format(w))
print("Number of remaining characters within the file: {}".format(r))
