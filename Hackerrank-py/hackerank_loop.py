def loop_square_num():
    n = int(input('Enter your integer:\t'))
    for num in range(n):
        res = num * num
        print(res)


# loop_square_num()


def leap_year():
    year = int(input('Enter your year:\t'))
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


print(leap_year())
