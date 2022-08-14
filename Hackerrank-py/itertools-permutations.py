from itertools import permutations


def gen_permutation():
    """
    itertools.permutations(iterable[, r]) is a tool that returns successive r length permutations
    of elements in an iterable.
    If r is not specified or is None, then r defaults to the length of the iterable, and all
    possible full length permutations are generated.

    TASK:
    You are given a string S.
    Your task is to print all possible permutations of size k of the string in
    lexicographic sorted order.

    INPUT FORMAT:
    A single line containing the space separated string S and the integer value k.

    Sample Input:
    HACK 2

    Sample Output:
    AC
    AH
    AK
    CA
    CH
    CK
    HA
    HC
    HK
    KA
    KC
    KH
    """

    string, perm_size = list(input().split(' '))

    print(f'String: {string}\nPermutation Size: {perm_size}')

    result_permutation = list(permutations(sorted(list(string)), int(perm_size)))

    for res in result_permutation:
        print(f"{''.join(res)}")

    return 'All Done!'


gen_permutation()
