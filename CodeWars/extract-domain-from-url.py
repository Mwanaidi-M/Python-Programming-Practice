import re


def domain_name(url):
    """
    Write a function that when given a URL as a string, parses out just the domain
    name and returns it as a string. For example:

    * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
    * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
    * url = "https://www.cnet.com"                -> domain name = cnet"
    """

    match_object = re.compile(r"""
    (http(s)?://)?      # check if the url has http:// or https:// (group 1 & 2)
    (www.)?             # check if the url has www. (group 3)
    ([A-Za-z0-9-]+)     # check if the url is followed up with a string/word (group 4)
    """, re.VERBOSE)

    # perform a search to find a match
    find_domain = re.search(match_object, url)

    # check if there is a match and if yes, return the 4th group match
    if find_domain:
        return find_domain.group(4)
