# Define a function named all_equal that takes a list and checks whether all elements
# in the list are the same.
# For example, calling all_equal([1, 1, 1]) should return True.

def all_equal(ls):
    return True if len(ls) == ls.count(ls[0]) else False

    # alternative technique
    # return all(val == ls[0] for val in ls)


print(all_equal([1, 1, 1]))
print(all_equal(["one", "one", "two"]))
