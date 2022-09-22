def array_diff(arr1, arr2):
    """
    Implement a difference function, which subtracts one list from another and
    returns the result.

    It should remove all values from list arr1, which are present in list arr2 keeping
    their order.

    array_diff([1,2],[1]) == [2]
    If a value is present in arr2, all of its occurrences must be removed from the other:

    array_diff([1,2,2,2,3],[2]) == [1,3]
    """
    return [num for num in arr1 if num not in arr2]