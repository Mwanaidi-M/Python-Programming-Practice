def is_anagram(test, original):
    """
    An anagram is the result of rearranging the letters of a word to produce a
    new word.
    Note: anagrams are case-insensitive

    Complete the function to return true if the two arguments given are anagrams
    of each other; return false otherwise.
    Examples
    "foefet" is an anagram of "toffee"

    "Buckethead" is an anagram of "DeathCubeK"
    """
    return sorted(test.lower()) == sorted(original.lower())
