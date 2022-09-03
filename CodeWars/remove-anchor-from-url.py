import re


def remove_url_anchor(url):
    """
    Complete the function/method so that it returns the url with anything after
    the anchor (#) removed.

    Examples:
    "www.codewars.com#about" --> "www.codewars.com"
    "www.codewars.com?page=1" -->"www.codewars.com?page=1"
    Args:
        url: <str>

    Returns:
        url_match_obj: <str>
    """

    # for the pattern, find the match/word/str(.*) that has '#' (?=#)[lookahead] after it.
    url_regex = re.compile(r".*(?=#)")

    url_match_obj = re.search(url_regex, url)

    # print(url_match_obj)
    if url_match_obj is None:
        return url
    else:
        return url_match_obj.group()


print(remove_url_anchor('www.codewars.com#about'))
# print(remove_url_anchor('www.codewars.com/katas/?page=1#about'))
