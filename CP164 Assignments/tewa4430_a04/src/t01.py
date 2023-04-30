'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-07"
-----------------------------------------------

'''
# Imports

from Food import Food
from Food_utilities import read_foods
from Queue_circular import Queue

fv = open('foods.txt', 'r')
  
foods = read_foods(fv)

q_ = Queue()

q_.insert(foods[1])
q_.insert(foods[0])
q_.insert(foods[1])
q_.insert(foods[2])

q_.remove()

for item in q_:
    print(item)

print("\nFront: {}".format(q_._front))
print("\nRear: {}".format(q_._rear))
print("\nCount: {}".format(q_._count))
