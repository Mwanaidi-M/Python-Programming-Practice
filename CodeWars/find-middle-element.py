def gimme(input_array):
    """
    You need to create a function that when provided with a triplet, returns the
    index of the numerical element that lies between the other two elements.

    The input to the function will be an array of three distinct numbers.

    For example:
    gimme([2, 3, 1]) => 0
    2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
    """
    new_array = input_array

    # print(sorted(new_array)[1])
    # print(input_array)
    return input_array.index(sorted(new_array)[1])


print(gimme([2, 3, 1]))
print(gimme([5, 10, 14]))
