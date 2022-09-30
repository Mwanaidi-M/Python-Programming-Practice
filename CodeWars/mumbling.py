"""
The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(strng):
    ls_st = []
    for ind in range(len(strng)):
        ls_st.append(strng[ind] * (ind+1))

    ls_st = [st.title() for st in ls_st]
    return '-'.join(ls_st)



print(accum("abcd"))
print(accum("RqaEzty"))