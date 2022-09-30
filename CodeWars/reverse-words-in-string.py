def reverse(st):
    """
    You need to write a function that reverses the words in a given string. A word can also fit an
    empty string. If this is not clear enough, here are some examples:

    As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

    Example (Input --> Output)

    "Hello World" --> "World Hello"
    "Hi There." --> "There. Hi"

    """

    # convert the string to a list
    st_ng = st.split(" ")

    # remove any unnecessary whitespace in the list
    st_ng = [wrd for wrd in st_ng if wrd != ""]

    # reverse the list then join it to a string
    new_st = " ".join(st_ng[::-1])

    return new_st


print(reverse('ylgehoqokhpahf   ikpdhwdgagykqiakulryeahrsqofruppkiys  esqa iykg upd'))
print(reverse("Hi There."))
