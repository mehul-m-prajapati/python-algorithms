#!/usr/bin/env python
def binary_search(L, v):
    """
    (list, object) -> int

    Precondition: L is sorted from smallest to largest, and
    all the items in L can be compared to v.

    Return the index of the first occurence of v in L,
    or return -1 if v is not in L.

    >>> binary_search([2, 3, 4, 5], 2)
    0
    >>> binary_search([2, 3, 4, 5], 4)
    2
    >>> binary_search([2, 3, 4, 5], 13)
    -1
    """
    base = 0
    end = len(L) - 1

    while base <= end:

        mid = (base + end) // 2
        
        if v > L[mid]:
            base = mid + 1
        elif v < L[mid]:
            end = mid - 1
        else:
            return mid
    
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
