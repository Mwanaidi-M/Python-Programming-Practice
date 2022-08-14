def filter_list(m_list):
    """
    create a function that takes a list of non-negative integers and strings and returns a
    new list with the strings filtered out.
    Example:
    filter_list([1,2,'a','b']) == [1,2]
    filter_list([1,'a','b',0,15]) == [1,0,15]
    Args:
        m_list: <list>
    Returns:
        <list>
    """

    # used the filter and lambda function and checked if the list object is not an instance of str
    # and return that restult as a list.
    return list(filter(lambda val: not isinstance(val, str), m_list))
