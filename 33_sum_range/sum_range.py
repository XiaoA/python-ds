def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """





    """My first thought was to use a `reduce` function. But even when Imported the library, I had issues.

    # return functools.reduce(nums)

    # I learned that the built-in `Sum` function would probably perform better.
    # Ref: https://docs.python.org/3/library/functions.html#sum
    # https://realpython.com/python-reduce-function/#comparing-reduce-and-accumulate

    # The SB implementation first checks for cases where there is no 'end', and returns the sum of the entire list, before slicing the start/end indices:
    """

    if end is None:
        end = len(nums)

    return sum(nums[start:end + 1])



   # When might the `reduce` function be a better approach? I'll need to look into that more.

    
