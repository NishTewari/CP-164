"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2020-04-02"
-------------------------------------------------------
"""
# Imports
from random import randint  
from Number import Number
from Sorts_array import Sorts

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
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    # Initialize Array
    values = []
    # Loop for SIZE
    for i in range(SIZE):
        # Create a Number object
        num = Number(i)
        # Add the Number object to the array
        values.append(num)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    # Initialize Array
    values = []
    # Loop for SIZE backwards
    for i in range(SIZE - 1, -1, -1):
        # Create a Number object using int i
        num = Number(i)
        # Add the Number object to the array
        values.append(num)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TEST rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    # Initialize Array
    arrays = []
    # Run through all rows
    for i in range(TESTS):
        # Create the columns
        arrays.append([])
        # Run through the current rows' column
        for j in range(SIZE):
            # Generate a random int from 0 to XRANGE
            ran = randint(0, XRANGE)
            # Create a Number object using the random int
            num = Number(ran)
            # Add the Number object to the 2D list
            arrays[i].append(num)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    count_a = 0
    count_b = 0
    count_c = 0
    swaps_c = 0
    
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
        swaps_c += Sorts.swaps
        for j in i:
            count_c += j.comparisons
        
        Number.comparisons = 0
        Sorts.swaps = 0
        
    swaps_c /= SIZE
    count_c /= (SIZE * TESTS)
    
    print("{:<14} {:8.0f} {:8.0f} {:8.0f} {:8.0f} {:8.0f} {:8.0f}".format(title, count_a, count_b, count_c, swaps_a, swaps_b, swaps_c))

    return
