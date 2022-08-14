import time

intro_msg = " THE A-B-C CHECKBOOK "
user_menu_option = ""
user_name = ""
user_amount = 0


def show_menu():
    print(f"{intro_msg:=^100}\n")
    print("1. Create account.")
    print("2. Deposit money to account.")
    print("3. Withdraw money from account.")
    print("4. Exit program.\n")


def name_rules():
    print("\nPlease note:")
    print("Your account name should have at least 4 letters.")
    print("Your account name should be one word.")
    print("Your account name should not contain any numbers.\n")


def deposit_rules():
    print("\nPlease note:")
    print("Minimum amount to deposit is 500.")


while user_menu_option != 4:
    show_menu()

else:
    print("Exiting program...")
    time.sleep(1)
    print("BYE!")
