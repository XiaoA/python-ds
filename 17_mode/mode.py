def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # I had to lean on the solution for this one. I started by trying to create a dictionary lookup, but kept getting lost in the weeds. This is kind of the concept I had in mind, so it made sense once I saw it...
    
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

        max_value = max(counts.values())
        for (num, freq) in counts.items():
            if freq == max_value:
                return num
