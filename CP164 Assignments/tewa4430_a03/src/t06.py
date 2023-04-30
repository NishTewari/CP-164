'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-30"
-----------------------------------------------

'''
from functions import postfix
string = input("Enter a string of operands and operators: ")
answer = postfix(string)
print("The answer is: {}".format(answer))
