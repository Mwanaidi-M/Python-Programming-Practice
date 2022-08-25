# A palindrome is a word, number, phrase, or other sequence of characters which reads the same
# backward as forward

def is_palindrome(strng):
    reverse_str = strng[::-1]

    return f"{strng} is a palindrome." if strng == reverse_str else f"{strng} is not a palindrome."


print(is_palindrome("kayak"))
print(is_palindrome("milk"))
