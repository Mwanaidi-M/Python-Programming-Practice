def perform_exception():
    """
    You are given two values val1 and val2.
    Perform integer division and print val1/val2.

    In the case of ZeroDivisionError or ValueError, print the error code.
    Note: For integer division in Python 3 use //.
    """

    num_cases = int(input('How many test cases do you want:\t'))

    for case in range(num_cases):
        val1, val2 = input().split(' ')

        try:
            res = int(val1) // int(val2)

        except ZeroDivisionError as z_error:
            print(f'Error Code: {z_error}')

        except ValueError as v_error:
            print(f'Error Code: {v_error}')
        else:
            print(res)


perform_exception()
