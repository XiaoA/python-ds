def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    # Initial attempt
    """check_vals = []

    for num in nums:
        while len(check_vals) > 3:
            val = nums.pop(0)
            check_vals.append(val)

        if check_vals[num] + num[i + 1] + num[i + 2] % 2 != 0:
            return True

    return False
    """
    
    # Returns erro: "IndexError: list index out of range"

    # My idea was to pop off the first three elements of a list, and add them up, and check if they're odd. Looking it it now, I can see that it wouldn't iterate through the entire list. And it could be done in place...

    # SB Approach:
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True

    return False
