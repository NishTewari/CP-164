'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-30"
-----------------------------------------------

'''
from Priority_Queue_array import Priority_Queue
pq = Priority_Queue()
pq.insert(11)
pq.insert(22)
pq.insert(33)
pq.insert(44)
pq.insert(55)
print("Priority Queue:")
for v in pq:
    print(v)
print()
pq.remove()
pq.remove()
print("Priority Queue")
for v in pq:
    print(v)
