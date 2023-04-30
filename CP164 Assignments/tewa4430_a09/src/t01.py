'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-04-02"
-----------------------------------------------

'''
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total

FILENAME = "miserables.txt"
hs = Hash_Set(20)
fv = open(FILENAME, "r", encoding="UTF-8")
insert_words(fv, hs)
fv.close()

total, maxword = comparison_total(hs)

print("Using array-based list HashSet")
print()
print("Total Comparisons: {:,d}".format(total))
print("Word with maximum comparisons '{}': {:,d}".format(
    maxword.word, maxword.comparisons))

