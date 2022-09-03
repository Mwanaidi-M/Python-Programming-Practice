# Create a method to see whether the string is ALL CAPS.
# Examples (input -> output):
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True

def is_uppercase(inp):
    # check if the string in uppercase is equal to the string input param given
    return inp.upper() == inp
