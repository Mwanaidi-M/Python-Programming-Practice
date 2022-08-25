# Write a function that takes a list of lists and flattens it into a one-dimensional list.
# Create a function flatten that takes a single parameter and return a list.
# For example, calling: flatten([[1, 2], [3, 4]]) should return the list: [1, 2, 3, 4]

def flatten(m_list):
    new_list = []

    for inner_list in m_list:
        for val in inner_list:
            new_list.append(val)

    return new_list


print(flatten([[1, 2], [3, 4]]))
