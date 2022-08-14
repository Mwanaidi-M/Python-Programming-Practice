def stingValidator():
    """Python has built-in string validation methods for basic data. It can check if a string is composed of 
        alphabetical characters, alphanumeric characters, digits, etc.

        Given a string S, your task is to find out if the string S contains any: alphanumeric characters, 
        alphabetical characters, digits, lowercase and uppercase characters.
    """
    string = input('Your String: \t')

    # check if any character in the string is an alphanumeric
    if any(s.isalnum() for s in string):
        print(True)
    else:
        print(False)
    # check if any character in the string is an alphabet
    if any(s.isalpha() for s in string):
        print(True)
    else:
        print(False)
    # check if any character in the string is a digit
    if any(s.isdigit() for s in string):
        print(True)
    else:
        print(False)
    # check if any character in the string is lowercase
    if any(s.islower() for s in string):
        print(True)
    else:
        print(False)
    # check if any character in the string is an uppercase
    if any(s.isupper() for s in string):
        print(True)
    else:
        print(False)

stingValidator()