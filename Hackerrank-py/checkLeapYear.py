def checkLeapYear(yr):
    '''
        This is a simple function to check whether a year is a leap year or not.
    '''

    if 1900 <= yr <= 10e5:
        if yr % 4 == 0:
            if yr % 100 == 0:
                if yr % 400 == 0:
                    return 'Leap Year'
                else:
                    return 'Not A Leap Year'
            else:
                return 'Leap Year'
        else:
            return 'Not a Leap Year'
    else:
        return 'This value is not within the limits'


print(checkLeapYear(2000))
print(checkLeapYear(2400))
print(checkLeapYear(1900))
print(checkLeapYear(1990))
print(checkLeapYear(1992))
