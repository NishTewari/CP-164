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
from utilities import array_to_queue, queue_to_array

queue = Queue()
source = [11, 22, 33, 44, 55]
target = []
array_to_queue(queue, source)
print("Queue:")
for i in queue:
    print(i)
    
print("Source: {}".format(source))
print()
queue_to_array(queue, target)
print("Queue:")
for i in queue:
    print(i)
print("Source: {}".format(target))
