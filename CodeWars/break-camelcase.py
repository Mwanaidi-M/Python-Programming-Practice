"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(my_string):
    # create a new string to hold the new updated string
    new_string = ''

    # loop through the characters of the string
    for st in my_string:
        # if the character is uppercase
        if st.isupper():
            # add a space to the character
            st = f' {st}'

        # add these characters to the new string
        new_string += st
    return new_string


print(solution("camelCasing"))
print(solution("breakCamelCase"))
