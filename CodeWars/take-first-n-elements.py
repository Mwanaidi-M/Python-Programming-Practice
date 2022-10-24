def take(arr,n):
    """
    Create a function that accepts a list/array and a number n, and returns
    a list/array of the first n elements from the list/array.
    """
    # alternative method
    # return arr[:n]
    return [ar for ar in arr[:n]]
