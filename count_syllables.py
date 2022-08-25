# Define a function named count that takes a single parameter. The parameter is a string.
# The string will contain a single word divided into syllables by hyphens, such as these:
# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.
# For example, the call count("ho-tel") should return 2.

def count(strng):
    st_list = strng.split("-")

    return len(st_list)


print(count("ho-tel"))