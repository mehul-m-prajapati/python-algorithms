#!/usr/bin/python
"""
    Selection Sort
    --------------
    Finiding the 1st minimum element from the list and putting it first. Then 2nd minimum to the 2nd and so on...
    .
    Time Complexity:  O(n**2)
    Space Complexity: O(1) Auxiliary
    Psuedo Code: http://en.wikipedia.org/wiki/Selection_sort
"""
def get_index_of_smallest(L, i):
    """
    (list, int) -> int

    Return the index of the smallest item in L[i:].

    >>> get_index_of_smallest([2, 4, 5, 3], 1)
    3
    """
    # The index of the smallest item so far.
    index_of_smallest = i
    length = len(L)

    for j in range(i + 1, length):
        if L[j] < L[index_of_smallest]:
            index_of_smallest = j

    return index_of_smallest

def sort(L):
    """
    (list of numbers) -> sorted list

    Takes a list of integers and sorts them in ascending order. This sorted list is then returned.

    >>> sort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    """
    length = len(L)

    for i in range(length):
        # Find the index of the smallest item in L[i:] and swap that
        # item with the item at index i
        index_of_smallest = get_index_of_smallest(L, i)
        L[index_of_smallest], L[i] = L[i], L[index_of_smallest]

    return L

if __name__ == "__main__":
    import doctest
    doctest.testmod()
