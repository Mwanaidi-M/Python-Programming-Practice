def index(arr, num):
    """
    You are given an array with positive numbers and a non-negative number num.
    You should find the num-th power of the element in the array with the index num.
    If num is outside the array, then return -1. Don't forget that the first element
    has the index 0.

    Examples:

    arr = [1, 2, 3, 4] and num = 2, then the result is 3^2 == 9;
    arr = [1, 2, 3] and num = 3, but num is outside the array, so the result is -1.
    """
    if len(arr) <=num:
        return -1
    else:
        return arr[num] ** num


print(index([1, 2, 3, 4], 2))
print(index([1, 2, 3], 3))
