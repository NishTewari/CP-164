'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-07"
-----------------------------------------------

'''
from Priority_Queue_array import Priority_Queue
from functions import pq_split_alt

source = Priority_Queue()

for i in range(12):
    source.insert(i)
    
target1, target2 = pq_split_alt(source)
print('Target 1')
for item in target1:
    print(item)  
print('\nTarget 2')  
for item in target2:
    print(item)
