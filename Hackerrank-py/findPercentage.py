def findPercentage():
    """You are required to read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
        Print the average of the marks array for the student name provided, showing 2 places after the decimal.

        Sample Input 0

            3
            Krishna 67 68 69
            Arjun 70 98 63
            Malika 52 56 60
            Malika

        Sample Output 0

            56.00
    """

    # determine the size of the input
    size = int(input('How many:\t'))

    # create an empty dictionary to hold the values
    student_marks = {}

    # loop through the given size range to allow input
    for s in range(size):
        # since input is given in one line, first make a variable to accept the input then split it
        line = input().split()

        # create two variables to hold the one line input, separating it into name and marks input by indexing the
        # 'line' var
        name, marks = line[0], line[1:]

        # convert the marks input to a float value
        marks = map(float, marks)

        # save the marks to the given name, the marks should be stored as a list
        student_marks[name] = list(marks)

    # ask the user to give a name of the student whose marks they want to calculate average.
    qname = input('Which student:\t')

    # store the marks of the query student in a variable
    scores = student_marks[qname]

    # calculate the average of the scores
    avg = sum(scores) / len(scores)
    print(student_marks)

    # display the average close to 2d.p like such
    print('{:.2f}'.format(avg))


findPercentage()
