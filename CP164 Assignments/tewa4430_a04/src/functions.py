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
from copy import deepcopy

from Priority_Queue_array import Priority_Queue


# Constants
def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    for _ in deepcopy(source):
        
        if (deepcopy(source.peek()) <= key):
            target1.insert(deepcopy(source.remove()))
        else:
            target2.insert(deepcopy(source.remove()))
    
    return target1, target2


def pq_split_alt(source):
    """
    -------------------------------------------------------
    Splits a priority queue into two with values going to alternating
    priority queues. The source priority queue is empty when the method
    ends. The order of the values in source is preserved.
    Use: target1, target2 = pq_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
    Returns:
        target1 - a priority queue that contains alternating values
            from source (Priority_Queue)
        target2 - priority queue that contains  alternating values
            from source (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    i = 0
    while not source.is_empty():
        if i % 2 == 0:
            target1.insert(deepcopy(source.remove()))
        else:
            target2.insert(deepcopy(source.remove()))
        i += 1
    return target1, target2


def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    total = 0
    edges = []
    nodes_checked = []
    all_node = graph.node_names()
    
    pq = Priority_Queue()
    for d in graph.edges_by_node(start_node):
        pq.insert(d)
    
    nodes_checked.append(start_node)
    edge = pq.remove()
    edges.append(edge)
    total += edge.distance
    nodes_checked.append(edge.end())
    node_next = edge.end()
    
    while len(nodes_checked) != len(all_node):
        for d in graph.edges_by_node(node_next):
            pq.insert(d)
            
        edge = pq.remove()
        
        while edge.end() in nodes_checked:
            edge = pq.remove()
            
        edges.append(edge)
        total += edge.distance
        nodes_checked.append(edge.end())
        node_next = edge.end()
        
    return edges, total
    
