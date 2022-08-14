import sys

example_email = 'InterviewBit@gmail.com'


def slice_email():
    """
    A function implementing an email slicer which is a simple tool that will take an email address
    as an input and slice it to produce the username and the domain associated with it. The email
    must be divided into two strings by using ‘@’ as the separator.

    Returns: Name & Domain
    """

    try:
        email = input("What is your email address:\t")
        name, domain = email.split('@')

    except:
        # using sys.exc_info() to get the exception that is produced
        print(f"{sys.exc_info()[0]}Incorrect Input.Please enter a valid email address")

    else:
        print(f'Name: {name}\nDomain: {domain}')


slice_email()
