'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-30"
-----------------------------------------------

'''
from Queue_array import Queue
q = Queue()
q.insert(100)
q.insert(140)
q.insert(159)
q.insert(192)
q.insert(215)
print("Queue")
for i in q:
    print(i)
print()
print("Queue after removing the values")
q.remove()
q.remove()
for i in q:
    print(i)
print()
value = q.peek()
print("Value at the peek: {}".format(value))
