'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-27"
-----------------------------------------------

'''
from List_linked import List
lst_link = List()
lst_link.append(3)
lst_link.prepend(6)
print("Linked list after appending and prepending")
for i in lst_link:
    print(i)
lst_link.insert(1, 29)
lst_link.insert(2, 83)
lst_link.insert(3, 36)
print("Linked List after inserting")
for j in lst_link:
    print(j)
  
