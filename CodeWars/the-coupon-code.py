"""
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat
the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed
as strings in this format: "MONTH DATE, YEAR".

Examples:
    checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
    checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
"""
import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    curr = datetime.datetime.strptime(current_date, '%B %d, %Y').date()
    exp = datetime.datetime.strptime(expiration_date, '%B %d, %Y').date()

    # print(f"{curr} ------ {exp}")
    return entered_code is correct_code and curr <= exp


check_coupon('123','123','September 5, 2014','October 1, 2014')
check_coupon('123a','123','September 5, 2014','October 1, 2014')
