def name_shuffler(str_):
    """
    Write a function that returns a string in which firstname is swapped with last name.

    Example(Input --> Output)

    "john McClane" --> "McClane john"
    """

    f_name, l_name = str_.split(" ")

    f_name, l_name = l_name, f_name
    return f"{f_name} {l_name}"


print(name_shuffler('john McClane'))
