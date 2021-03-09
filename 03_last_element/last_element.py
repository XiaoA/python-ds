def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # My original solution:

    # if len(lst) == 0:
    #     return None

    # return lst[-1]

    ## Functions return None by default, so we can simplify it:

    if lst:
        return lst[-1]
    
    
