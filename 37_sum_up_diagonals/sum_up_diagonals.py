def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # I have to admit, I struggled with this one. I found some solutions that used the numby library, but I wasn't able to coe up with a good solution. I need to brush up on my matrix algebra...

    # SB approach
    total = 0
    
    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]
        
    return total
    
