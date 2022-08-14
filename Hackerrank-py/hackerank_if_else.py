def if_else(n):
    """
        Given an integer,n , perform the following conditional actions:

        If n is odd, print Weird
        If n is even and in the inclusive range of 2 to 5, print Not Weird
        If n is even and in the inclusive range of 6 to 20, print Weird
        If n is even and greater than 20, print Not Weird
    """
    n = int(n)
    if n % 2 != 0:
        return 'Weird'
    elif n % 2 == 0 and n in range(2, 6):  # have the range from 2-6 so as to include 5
        return 'Not Weird'
    elif n % 2 == 0 and n in range(6, 21):  # have the range from 6-21 so as to include 20 5
        return 'Weird'
    elif n % 2 == 0 and n > 20:
        return 'Not Weird'


print(if_else(3))
print(if_else(24))
