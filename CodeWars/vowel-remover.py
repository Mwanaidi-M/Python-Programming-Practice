"""
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
"""


def shortcut(st):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_st = ''
    for s in st:
        if s not in vowels:
            new_st += s

    return new_st


print(shortcut('codewars'))
