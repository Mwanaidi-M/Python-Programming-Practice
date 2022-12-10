"""
Find the mean (average) of a list of numbers in an array.

To find the mean (average) of a set of numbers add all the numbers together and divide by the
number of values in the list.

For an example list of 1, 3, 5, 7: The mean (or average) of this list is 4
"""


def find_average(nums):
    return sum(nums) / len(nums) if len(nums) > 0 else 0
