def mid(strng):
    """
    Function that takes a string as its parameter. The function should extract and return
    the middle letter. If there is no middle letter, your function should return the empty string.

    For example, mid("abc") should return "b" and mid("aaaa") should return "".
    Args:
        strng: <str>
    Returns:
        lett: <str>
    """

    # check if the string length is even, then return an empty string, else use the floor division to get
    # the average value and use it as the index to get the letter in the middle.
    if len(strng) % 2 == 0:
        return ""
    else:
        mid_num = len(strng) // 2
        return strng[mid_num]


print(mid("ac"))
print(mid("abc"))
# print(mid("aaaa"))
