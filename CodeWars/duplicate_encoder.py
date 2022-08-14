def duplicate_encode(word):
    """
    The goal of this exercise is to convert a string to a new string where each character
     in the new string is "(" if that character appears only once in the original string,
     or ")" if that character appears more than once in the original string. Ignore
     capitalization when determining if a character is a duplicate.

    Examples
    "din"      =>  "((("
    "recede"   =>  "()()()"
    "Success"  =>  ")())())"
    "(( @"     =>  "))(("
    Args:
        word: str

    Returns: str

    """
    # Convert the word to lower case as a whole
    word_lower = word.lower()

    return ''.join(['(' if word_lower.count(letter) == 1 else ')' for letter in word_lower])


print(duplicate_encode('din'))
print(duplicate_encode('Success'))
print(duplicate_encode('(( @'))
