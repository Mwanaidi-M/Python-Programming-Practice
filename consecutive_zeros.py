# The goal of this challenge is to analyze a binary string consisting of only zeros and
# ones. Your code should find the biggest number of consecutive zeros in the string. For
# example, given the string: "1001101000110" the biggest number of consecutive zeros is 3.

def consecutive_0s(b_num):
    z_list = b_num.split("1")

    return len(max(z_list))
