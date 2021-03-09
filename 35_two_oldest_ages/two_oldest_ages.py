def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    # My first strategy was to create a tuple of sorted ages. Unfortunately, I forgot to account for duplicate values:
    
    
    """Failed example:
    # return tuple(sorted(ages)[-2:])

    two_oldest_ages([1, 5, 5, 2])
  
    Expected:
        (2, 5)
    Got:
        (5, 5)
    """

    # Creating a set of ages first fixes the problem, by creating a unique set of values:

    ages_set = set(ages)
    return tuple(sorted(ages_set)[-2:])
