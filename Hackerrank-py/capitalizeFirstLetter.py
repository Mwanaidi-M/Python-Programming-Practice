def capitalize_first_letter(word):
    """You are asked to ensure that the first and last names of people begin with a 
       capital letter in their passports. 

    Args:
        word ([str]): A single line of input containing the full name.
                        Note: in a word only the first character is capitalized. Example 12abc 
                        when capitalized remains 12abc.
    """

    new_list = []  # list to hold the capitalized words
    for st in word.split(' '):  # split the input where there is a space
        new_list.append(st.capitalize())  # append the capitalized word to the new list

    return ' '.join(new_list)  # return a single string of the list.
