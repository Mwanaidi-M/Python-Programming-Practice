def is_divide_by(number, a, b):
    """
    create the functionisDivideBy (or is_divide_by) to check if an integer number is divisible by both integers a and b.

    A few cases:

    (-12, 2, -6)  ->  true
    (-12, 2, -5)  ->  false

    (45, 1, 6)    ->  false
    (45, 5, 15)   ->  true

    (4, 1, 4)     ->  true
    (15, -5, 3)   ->  true
    Args:
        number: <int>
        a:<int>
        b:<int>

    Returns:
        <bool>
    """
    return True if (number % a == 0 and number % b == 0) else False
