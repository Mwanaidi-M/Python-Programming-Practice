"""
Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in the same order.
"h,o,l,a"
"""


def print_array(arr):
    arr = [str(a) for a in arr]
    return ','.join(arr)


print(print_array([2]))
print(print_array([2, 4, 5, 2]))
print(print_array([2.0, 4.2, 5.1, 2.2]))
print(print_array(["2", "4", "5", "2"]))
print(print_array([True, False, False]))

