from functools import reduce
import logging


def factorial(num):
    """
    In mathematics, the factorial of a non-negative integer num, denoted by num!,
    is the product of all positive integers less than or equal to n.
    For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

    Write a function to calculate factorial for a given input. If input is below 0 or
    above 12 throw an exception of type ValueError (Python).
    """
    if num < 0 or num > 12:
        raise ValueError
    else:
        nums = list(range(1, num + 1))
        result = reduce(lambda num1, num2: num1 * num2, nums)

    return result


# factorial method type 2
def factorial_2(num):
    if num < 0 or num > 12:
        raise ValueError

    return 1 if num <= 1 else num * factorial_2(num - 1)


# factorial method type 3
def factorial_3(num):
    if num < 0 or num > 12:
        raise ValueError
    total = 1
    for n in range(1, num + 1):
        total *= n

    return total


# print(factorial(5))
# print(factorial_2(5))
print(factorial_3(7))

