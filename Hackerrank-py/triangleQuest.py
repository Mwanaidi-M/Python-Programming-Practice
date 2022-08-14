def triangle_quest():
    """You are given a positive integer N . Print a numerical triangle of height N-1  like the one below:
    
        1
        22
        333
        4444
        55555
    """
    size = int(input('Enter your size: \t'))
    # for num in range(size):
    #     for n in range(num):
    #         print(num, end=' ')
    #     print()

    # Found a simple method to achieve this triangle
    for num in range(1, size):
        print(str(num) * num)

    # If you wish to use a pure math method
    for num in range(1, size):
        print((10 ** num // 9) * num)


triangle_quest()
