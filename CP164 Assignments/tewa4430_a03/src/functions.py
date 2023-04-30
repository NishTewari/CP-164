'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-01-30"
-----------------------------------------------

'''
# Imports
from Stack_array import Stack
# Constants


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    i = 0
    
    while source.is_empty() == False:
        if i % 2 == 0:
            target1.push(source.pop())
            i += 1
        elif i % 2 != 0:
            target2.push(source.pop())
            i += 1
        return target1, target2
            
            
def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    temp = 0
    while source1.is_empty() == False or source2.is_empty() == False:
        if source1.is_empty == False and source2.is_empty == False:
            if temp % 2 == 0:
                target.push(source1.pop())
            else:
                target.push(source2.pop()) 
        elif source1.is_empty():
            target.push(source2.pop())
        elif source2.is_empty():
            target.push(source1.pop())
        temp += 1
    return target


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    n_str = ""
    index_value = 0
    for i in string.lower():
        if i.isalpha() == True:
            n_str += i
    
    middle_value = len(n_str) // 2
    string_stack = Stack()
    
    while index_value < middle_value:
        string_stack.push(n_str[index_value])
        index_value += 1
    
    if len(n_str) % 2 != 0:
        index_value += 1
    
    while index_value < len(n_str):
        if n_str[index_value] != string_stack.pop():
            palindrome = False
        index_value += 1
    return palindrome


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    v_stack = Stack()
    string = string.split()
    for i in string:
        if i not in OPERATORS:
            v_stack.push(i)
        else:
            if i == "+":
                first_value = v_stack.pop()
                second_value = v_stack.pop()
                new_value = int(second_value) + int(first_value)
                v_stack.push(str(new_value))
            elif i == "-":
                first_value = v_stack.pop()
                second_value = v_stack.pop()
                new_value = int(second_value) - int(first_value)
                v_stack.push(str(new_value))
            elif i == "*":
                first_value = v_stack.pop()
                second_value = v_stack.pop()
                new_value = int(second_value) * int(first_value)
                v_stack.push(str(new_value))
            elif i == "/":
                first_value = v_stack.pop()
                second_value = v_stack.pop()
                new_value = int(second_value) / int(first_value)
                v_stack.push(str(new_value))
    answer = v_stack.pop()
    return answer

    
def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = 0
    return path
