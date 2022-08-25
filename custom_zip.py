# The built-in zip function "zips" two lists. Write your own implementation of this function. Define
# a function named zap. The function takes two parameters, a and b. These are lists. Your function
# should return a list of tuples. Each tuple should contain one item from the list a and one from b.
# You may assume a and b have equal lengths.

def zap(a, b):
    # create empty list to hold the tuples
    ml = []

    # loop through the size of one list and create a tuple of items in list a & b
    for num in range(len(a)):
        ml.append((a[num], b[num]))

    return ml


print(zap([0, 1, 2, 3], [5, 6, 7, 8]))
