'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-03-26"
-----------------------------------------------

'''
# Imports

# Constants


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Use:
    Do not create an actual Hash_Set.
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    
    print("Hashes")
    print("Hash     Slot Key")
    print("======== ==== ====================")
    for b in values:
        h = hash(b)
        slot = h % slots
        print("{:>8d} {:>4} {:s}".format(h, slot, b.key()))
    return None
