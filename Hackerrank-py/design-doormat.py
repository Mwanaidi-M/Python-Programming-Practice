def doormat():
    """
    Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door
    mat with the following specifications:

    Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

    Sample Designs:

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
    """
    length = int(input('What is the length size:\t'))
    w = length * 3

    for i in range(1, length, 2):
        print((i * '.|.').center(w, '-'))
    print('WELCOME'.center(w, '-'))
    for v in range(length - 2, -1, -2):
        print((v * '.|.').center(w, '-'))


doormat()
