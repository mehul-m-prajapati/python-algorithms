#!/usr/bin/python
"""
    Bubble Sort
    -----------
    A naive sorting that compares and swaps adjacent elements.
    
    Time Complexity: O(n**2)
    Space Complexity: O(1) Auxiliary
    Stable: Yes
    Psuedo code: http://en.wikipedia.org/wiki/Bubble_sort
"""
def sort(seq):
    """
    (list of numbers) -> sorted list

    Takes a list of integers and sorts them in ascending order. This sorted list is then returned.

    >>> sort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    >>> sort([14, 12, 10, 9])
    [9, 10, 12, 14]
    """
    L = len(seq)

    for i in range(L):
      for n in range(1, L - i):
	if seq[n] < seq[n - 1]:
	   seq[n], seq[n - 1] = seq[n - 1], seq[n]

    return seq

if __name__ == "__main__":
    import doctest
    doctest.testmod()
