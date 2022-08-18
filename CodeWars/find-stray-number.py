def stray(arr):
    """
    Given an odd-length array of integers, in which all of them are the same, except for one single number,
    complete the method which accepts such an array, and returns that single different number.

    The input array will always be valid! (odd-length >= 3)

    Examples
    [1, 1, 2] ==> 2
    [17, 17, 3, 17, 17, 17, 17] ==> 3
    Args:
        arr: <list>
    Returns:
        stray_num: <int>
    """

    for item in arr:
        if arr.count(item) == 1:
            return item


print(stray([1, 1, 1, 1, 1, 1, 2]))
