def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for element in lst:
        if not isinstance(element, list):
            return False

    return True
    

        # SB Alternative:
        # Alternate possibilities: use all() with a generator comprehension,
        # though that isn't something we've covered yet:
        #
        # return all(isinstance(item, list) for item in lst)

