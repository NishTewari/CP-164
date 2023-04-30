'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-04-02"
-----------------------------------------------

'''
# Imports
from Word import Word


def insert_words(file_variable, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number 
    of comparisons required to insert that Word object from 
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        hash_set - the HashSet to insert the words into (HashSet)
    Returns:
        None
    -------------------------------------------------------
    """
    file_variable.seek(0)

    for line in file_variable:
        words = line.split()

        for word in words:
            word = word.strip().lower()

            if word.isalpha():
                hash_set.insert(Word(word))
    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (HashSet)
    Returns:
        total - the total of all comparison fields in the HashSet
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = Word('q')

    for word in hash_set:
        total += word.comparisons

        if word.comparisons > max_word.comparisons:
            max_word = word
    return total, max_word
