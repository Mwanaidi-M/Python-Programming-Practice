"""
GRADE BOOK
Complete the function so that it finds the average of the three scores passed to it and
returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	    'F'

Tested values are all between 0 and 100. There's no need to check for negative values or values
greater than 100.
"""


def get_grade(val1, val2, val3):
    avg = int(sum([val1, val2, val3]) / 3)
    grade = ''

    if 90 <= avg <= 100:
        grade = 'A'
    elif 80 <= avg <= 90:
        grade = 'B'
    elif 70 <= avg <= 80:
        grade = 'C'
    elif 60 <= avg <= 70:
        grade = 'D'
    elif 0 <= avg <= 60:
        grade = 'F'

    return grade


print(get_grade(100, 85, 96))
print(get_grade(75, 70, 79))
