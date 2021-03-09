"""Sometimes, I think too far 'inside the box' on these kinds of problems. I thought the best (naive) way would be to split the integers, sort the integers, rejoin them, and then compare the count. It was not the most efficient, but simple. I couldn't find a way to iterate over the integers to make it work.' SB's solution was to create a method that returns a counter. This was obvious, but I wasn't thinking of creatin another method. (Derp!)
"""

def freq_counter(coll):
    """Returns frequency counter mapping of coll."""

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    
    """
    return freq_counter(str(num1)) == freq_counter(str(num2))
