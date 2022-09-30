def reverse_seq(n):
    """
    Build a function that returns an array of integers from n to 1 where n>0.

    Example : n=5 --> [5,4,3,2,1]
    """
    return [num for num in range(n, 0, -1)]