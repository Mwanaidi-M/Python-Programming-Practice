def sequence_sum(begin_number, end_number, step):
    """
    Your task is to make function, which returns the sum of a sequence of integers.
    The sequence is defined by 3 non-negative values: begin, end, step (inclusive).
    If begin value is greater than the end, function should return 0

    Examples:
    2,2,2 --> 2
    2,6,2 --> 12 (2 + 4 + 6)
    1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
    1,5,3  --> 5 (1 + 4)
    
    Args:
        begin_number: <int>
        end_number: <int>
        step: <int>

    Returns:
        result: <int>
    """
    result = sum(range(begin_number, end_number + 1, step))
    return result
