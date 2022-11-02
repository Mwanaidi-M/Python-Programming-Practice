"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even,
return the middle 2 characters.

Examples:
Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
"""


def get_middle(st):
    st_len = len(st)

    if st_len%2 == 0:
        mid = st_len // 2
        return st[mid-1:mid+1]
    else:
        mid = st_len // 2
        return st[mid]


print(get_middle("A"))
print(get_middle("middle"))
print(get_middle("test"))
