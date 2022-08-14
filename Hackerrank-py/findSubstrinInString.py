def find_string(string, sub_string):
    """Given a string and a sub-string, the task is to get the count of overlapping substring from the given string

    Args:
        string ([str]): [the string that you want to traverse through]
        sub_string ([str]): [the part of string you want to find the number of times it occurs]

    Returns:
        [int]: [the number of times the substring occurs in the string; including the overlapping substring]
    """
    # Initialize count and start to 0 
    count = 0
    start = 0

    # search through the string until you reach the end
    while start < len(string):
        # check if the substring is present from the 'start' position till the end
        position = string.find(sub_string, start)

        if position != -1:
            # If a substring is present, move 'start' to the next position from start of the substring 
            start = position + 1

            # increase the count
            count += 1

        else:
            # if no substring is present any further, then stop the loop
            break
    # return the value of the count
    return count


print(find_string('ABCDCDC', 'CDC'))