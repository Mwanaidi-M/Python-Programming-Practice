# Two strings are anagrams if you can make one from the other by rearranging the letters.

def is_anagram(str1, str2):
    """
    Function to check if str1 & str2 are anagrams
    Args:
        str1: <str>
        str2: <str>
    Returns:
        ans: <bool>
    """

    # convert str1 & str2 to lowercase first
    str1 = str1.lower()
    str2 = str2.lower()

    # used the sorted() function to check if both strings match
    return True if sorted(str1) == sorted(str2) else False


print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))
