'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-06"
-----------------------------------------------

'''
from List_array import List
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
from Stack_array import Stack


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    source1 = source[::-1]
    i = 0
    
    while i < len(source1):
        stack.push(source1[i])
        source.remove(source1[i])
        i += 1
    
    return None


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while stack.is_empty() == False:
        target.append(stack.pop())
    target = target.reverse()
    return None


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    print("Creating a new stack!")
    s = Stack()
    print()
    check_empty = s.is_empty()
    print("Empty stack? {}".format(check_empty))
    print()
    for i in range(len(source)):
        s.push(source[i])
        print("""Pushed:
        {}""".format(source[i]))
        print()
    value = s.peek()
    print("Value at the top: {}".format(value))
    s.push(value)
    print()
    print("Pushing {} onto the stack".format(value))
    print()
    check_empty = s.is_empty()
    print("Empty stack? {}".format(check_empty))
    print()
    value = s.pop()
    print("Popping first item from stack!")
    print()
    print("{} has been removed from the top of the stack!".format(value))
    check_empty = s.is_empty()
    print("Empty stack? {}".format(check_empty))
    return None


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    
    while i < len(source):
        queue.insert(source[i])
        source.remove(source[i])
    
    return None
    

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while queue.is_empty() == False:
        target.append(queue.remove())
    
    return None


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i < len(source):
        pq.insert(source[i])
        source.remove(source[i])
    return None


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while pq.is_empty() == False:
        target.append(pq.remove())
    return None


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    print("Creating a new queue!")
    q = Queue()
    check_empty = q.is_empty()
    print("\nEmpty stack? {}".format(check_empty))
    for i in range(len(a)):
        q.insert(a[i])
        print("""\nPushed:
        {}""".format(a[i]))
    value = q.peek()
    print("\nValue at the top: {}".format(value))
    q.insert(value)
    print("\nPushing {} onto the stack".format(value))
    check_empty = q.is_empty()
    print("\nEmpty stack? {}".format(check_empty))
    value = q.remove()
    print("\nPopping first item from stack!")
    print("\n{} has been removed from the top of the stack!".format(value))
    check_empty = q.is_empty()
    print("Empty stack? {}".format(check_empty))

    return None


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand
    print("Creating a new queue!")
    pq = Priority_Queue()
    check_empty = pq.is_empty()
    print("\nEmpty stack? {}".format(check_empty))
    for i in range(len(a)):
        pq.insert(a[i])
        print("""\nPushed:
        {}""".format(a[i]))
    value = pq.peek()
    print("\nValue at the top: {}".format(value))
    pq.insert(value)
    print("\nPushing {} onto the stack".format(value))
    check_empty = pq.is_empty()
    print("\nEmpty stack? {}".format(check_empty))
    value = pq.remove()
    print("\nPopping first item from stack!")
    print("\n{} has been removed from the top of the stack!".format(value))
    check_empty = pq.is_empty()
    print("Empty stack? {}".format(check_empty))

    return None


# Lab 4 Question 6
def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i < len(source):
        llist.append(source[i])
        source.remove(source[i])
    return None


# Lab 4 Question 6
def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i < len(llist):
        target.append(llist.remove(llist[i]))
    return None
    
    
def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    print("Creating a new list!")
    lst = List()
    print()
    check_empty = lst.is_empty()
    print("Empty list? {}".format(check_empty))
    print()
    for i in range(len(source)):
        lst.append(source[i])
        print("""Appended:
        {}""".format(source[i]))
        print()
    value = lst.peek()
    print("First value in the list: {}".format(value))
    lst.append(value)
    print()
    print("Appending {} in the stack".format(value))
    print()
    check_empty = lst.is_empty()
    print("Empty list? {}".format(check_empty))
    print()
    value = list.remove()
    print("Removing  first item from list!")
    print()
    print("{} has been removed from the first of the list!".format(value))
    check_empty = list.is_empty()
    print("Empty list? {}".format(check_empty))
    value = lst.insert(0, 3)
    print("Inserting 3 to the index 0")
    value_min = lst.min()
    print("Mininmum value of the list is : {}".format(value_min))
    value_max = lst.max()
    print("Maximum value of the list is : {}".format(value_max))
    value_find = lst.find(3)
    print("Finding the value: {}".format(value_find))
    value_index = lst.index(1)
    value_count = lst.count(1)

    return None

    return None
