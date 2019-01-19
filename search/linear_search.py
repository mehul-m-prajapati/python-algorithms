#!/usr/bin/env python
def linear_search(L, v):
    """
    (list, object) -> int

    Return the index of the first occurence of v in L,
    or return -1 if v is not in L.

    >>> linear_search([2, 3, 4, 5], 2)
    0
    >>> linear_search([2, 3, 4, 5], 4)
    2
    >>> linear_search([2, 3, 4, 5], 13)
    -1
    """
    for item in L:
        if item == v:
            return L.index(v)

    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
