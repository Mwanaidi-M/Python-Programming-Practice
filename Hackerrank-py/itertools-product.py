from itertools import product


def generate_product():
    """
    itertools.product() is a tool that computes the cartesian product of input iterables.
    It is equivalent to nested for-loops.
    You are given two lists A and B. Your task is to compute their cartesian product AxB.

    Example:
    A = [1, 2]
    B = [3, 4]
    AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

    Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.
    Returns:
    """

    a_list = list(map(int, input('Please input your values for the 1st list:\t').split(' ')))
    b_list = list(map(int, input('Please input your values for the 2st list:\t').split(' ')))

    print(f'List 1: {a_list}\nList 2: {b_list}')
    result_product = list(product(sorted(a_list), sorted(b_list)))

    for res in result_product:
        print(res, end=' ')
    print('\n')

    return 'All Done!'


print(generate_product())
