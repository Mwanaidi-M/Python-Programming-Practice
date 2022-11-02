"""
Given an array of integers, find the pair of adjacent elements that has the largest
product and return that product.

Example:

For inputArray = [3, 6, -2, -5, 7, 3], the output should be solution(inputArray) = 21.
7 and 3 produce the largest product.
"""


def solution(input_array):
    # list to hold product of adjacent elements
    prod_arr = []

    # looping through the indices of the input_array, calculating the product of adjacent items
    # append them to the list prod_arr
    for ind in range(len(input_array) - 1):
        prod_arr.append(input_array[ind] * input_array[ind + 1])

    # return the maximum value in the list
    return max(prod_arr)
