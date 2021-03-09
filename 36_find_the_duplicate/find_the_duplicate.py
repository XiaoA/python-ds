def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # My approach was on the right track, but failed in the case of no duplicates

    """duplicate_set = set()

    for num in nums:
        if num not in duplicate_set:
            duplicate_set.add(num)
            return duplicate_set
        elif len(duplicate_set) == 0:
            return None

    return duplicate_set
    """

    # SB approach, using 'positive' logic:
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)
 
