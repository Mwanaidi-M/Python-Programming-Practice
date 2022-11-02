"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF'].

The input will be a lowercase string with no spaces.
"""


def capitalize(st):
    even = ''
    odd = ''

    for ind in range(len(st)):
        char = st[ind]
        if ind % 2 == 0:
            char = st[ind].capitalize()
        even += char

    for ind in range(len(st)):
        char = st[ind]
        if ind % 2 != 0:
            char = st[ind].capitalize()
        odd += char

    return [even, odd]


print(capitalize("abracadabra"))
