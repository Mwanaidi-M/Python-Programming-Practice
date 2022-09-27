import string


def is_pangram(u_str):
    """
    A pangram is a sentence that contains every single letter of the alphabet at least once.
    For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it
    uses the letters A-Z at least once (case is irrelevant).

    Given a string, detect whether it is a pangram. Return True if it is, False if not.
    Ignore numbers and punctuation.
    """

    # creating a list of punctuation marks & numbers
    punc_marks = list(string.punctuation)
    nums = list(string.digits)

    # set for the alphabetical letters in lowercase
    lower_lett = set(string.ascii_lowercase)

    # removing spaces from the string
    u_str = u_str.replace(" ", "")
    new_s = set()

    # looping through the string, checking if the characters are not punctuation marks & numbers,
    # adding them to the set new_s
    for s in u_str.lower():
        if s not in punc_marks and s not in nums:
            new_s.add(s)

    # returning True or False if the sets are equal
    return lower_lett == new_s


pangram = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"

print(is_pangram(pangram))
