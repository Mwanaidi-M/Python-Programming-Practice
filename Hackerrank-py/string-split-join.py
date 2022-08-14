def split_and_join(line):
    """
    You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
    :param line: str
    :return: str
    """
    return '-'.join(line.split())
