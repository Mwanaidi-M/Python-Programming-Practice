def second_lowest_score():
    """
    Given the names and grades for each student in a class of N students, store them in a nested
    list and print the name(s) of any student(s) having the second-lowest grade.
    Note: If there are multiple students with the second-lowest grade, order their names
    alphabetically and print each name on a new line.
    Example Sample Input:
    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39

    Example Sample Output:
    Berry
    Harry
    """

    # get the number of students user will enter
    records_size = int(input('What is the number of students:\t'))

    # initialize the lists for records and all scores
    all_students = []
    all_scores = []

    # loop through the size and for each input append it to the corresponding list
    for record in range(records_size):
        name = input('What is the student name:\t')
        score = float(input('What is the student score:\t'))

        all_students.append([name, score])
        all_scores.append(score)

    # sort the list so that the names are organized alphabetically.
    all_students.sort()

    # convert the score's list to a set to remove duplicates then back to a list and sort it.
    list_score = list(set(all_scores))
    list_score.sort()

    # loop through the records and check if the second-lowest value is in the list then print that name.
    for student in all_students:
        if student[1] in student:
            print(student[0])

    # print(all_students)
    # print(all_scores)
    # print(list_score)


second_lowest_score()

