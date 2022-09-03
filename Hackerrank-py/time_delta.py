# When users post an update on social media,such as a URL, image, status update etc. other users
# in their network are able to view this new post on their news feed. Users can also see exactly
# when the post was published, i.e, how many hours, minutes or seconds ago. Since sometimes posts are
# published and viewed in different time zones, this can be confusing. You are given two timestamps
# of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Your task is to print the absolute difference (in seconds) between them.

# Input Format:
# The first line contains , the number of testcases.
# Each testcase contains  lines, representing time  and time .

# Output Format: Print the absolute difference  in seconds.

# Sample Input 0:
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# Sample Output 0:
# 25200
# 88200

import datetime


def sec_difference():
    """
    Function to print the absolute difference in seconds between given date values
    Returns:
        diff_sec: <class 'datetime.timedelta'>
    """

    num_testcases = int(input("How many test cases do you have?\t"))

    all_dates = []
    all_difference = []

    for num in range(num_testcases):
        date1 = input("Enter date1:\t")
        date2 = input("Enter date2:\t")

        date1 = datetime.datetime.strptime(date1, "%a %d %b %Y %H:%M:%S %z")
        date2 = datetime.datetime.strptime(date2,  "%a %d %b %Y %H:%M:%S %z")

        all_dates.append([date1, date2])

    for dates in all_dates:
        abs_diff = dates[0] - dates[1]
        all_difference.append(str(abs(int(abs_diff.total_seconds()))))

    print(all_dates)
    print(all_difference)

    return "\n".join(all_difference)


print(sec_difference())
