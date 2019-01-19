#!/usr/bin/python
"""
    Insertion Sort
    --------------
    Inserting unsorted elements into the sorted list.
    
    Time Complexity: O(n**2)
    Space Complexity: O(n) total
    Stable: Yes
    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.
"""
def insert(L, i):
    """ (list, int) -> NoneType
    
    Precondition: L[:i] is sorted from smallest to largest.
    
    Move L[i] to where it belongs in L[:i + 1]

    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """
    # The value to be inserted into the sorted part of the list
    val = L[i]

    # Find the index, j, where the value belongs.
    # Make room for the value by shifting.
    j = i

    while j != 0 and L[j - 1] > val:
        # Shift L[j - 1] one position to the right to L[j].
        L[j] = L[j - 1]
        j = j - 1

    L[j] = val

def sort(seq):
    """
    (list of numbers) -> sorted list

    Takes a list of integers and sorts them in ascending order. This sorted list is then returned.

    >>> sort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    """
    L = len(seq)

    for i in range(L):
        insert(seq, i)

    return seq

# Main function
if __name__ == "__main__":
    import doctest
    doctest.testmod()
