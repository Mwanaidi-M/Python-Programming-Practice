def count_positives_sum_negatives(arr):
    """
    Given an array of integers.
    Return an array, where the first element is the count of positives numbers and the
    second element is sum of negative numbers. 0 is neither positive nor negative.
    If the input is an empty array or is null, return an empty array.

    Example
    For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
    you should return [10, -65].
    Args:
        arr: <list>

    Returns:
        sum_arr: <list>
    """

    sum_neg = []    # array to hold sum of negative values
    count_pos = []    # array to hold count of positive values

    if len(arr) == 0:
        return []
    else:
        for arr_item in arr:
            if arr_item < 0:
                sum_neg.append(arr_item)
            elif arr_item != 0:
                count_pos.append(arr.count(arr_item))

        # print(sum_neg, sum_pos)
        return [len(count_pos), sum(sum_neg)]


my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

print(count_positives_sum_negatives(my_arr))
