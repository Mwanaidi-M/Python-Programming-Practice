"""
Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".
"""


def reverse_letter(string):
    string = string[::-1]
    new_string = ''.join([st for st in string if st.isalpha()])
    return new_string


print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
print(reverse_letter("ab23c"))
