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

from Priority_Queue_array import Priority_Queue
source = Priority_Queue()

for i in range(15):
    source.insert(i)
    
target1, target2 = source.split_alt()
print('Target 1')
for item in target1:
    print(item)  
print('\nTarget 2')  
for item in target2:
    print(item) 
