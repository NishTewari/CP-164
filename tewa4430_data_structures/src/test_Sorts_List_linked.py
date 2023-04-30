"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2020-04-02"
-------------------------------------------------------
"""
# Imports
import random
 
from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(0, SIZE):
        number = Number(i)
        values.append(number)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE - 1, -1, -1):
        number = Number(i)
        values.append(number)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = []
    
    for i in range(0, TESTS):
        arrays = List()
        lists.append(arrays)
    
    for j in lists:
        for k in range(0, SIZE):
            num = random.randrange(XRANGE)
            number = Number(num)
            j.append(number)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    
    count_a = 0
    count_b = 0
    count_c = 0
    
    list_a = create_sorted()
    func(list_a)
    swaps_a = Sorts.swaps
    
    for i in list_a:
        count_a += i.comparisons
    count_a /= SIZE
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    list_b = create_reversed()
    func(list_b)
    swaps_b = Sorts.swaps
    
    for i in list_b:
        count_b += i.comparisons
    count_b /= SIZE
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    list_c = create_randoms()
    
    for i in list_c:
        func(i)
        swaps_c = Sorts.swaps
        for j in i:
            count_c += j.comparisons
        
        Number.comparisons = 0
        Sorts.swaps = 0
        
    count_c /= (SIZE * TESTS)
    
    print("{:<14} {:8.0f} {:8.0f} {:8.0f} {:8.0f} {:8.0f} {:8.0f}".format(title, count_a, count_b, count_c, swaps_a, swaps_b, swaps_c))

    return
