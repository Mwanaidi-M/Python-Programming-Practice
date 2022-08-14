import os


def create_acc(acc_name, initial_deposit):
    """
    Function to create a new account and add it to a file.
    Args:
        acc_name: <str>
        initial_deposit: <int>

    Returns:
        Success message when account is created successfully.
    """
    # check if the account name file has been created already
    if os.path.exists(fr"D:\Python_Pracs\bank_checkbook\{acc_name}.txt"):
        print("This account name already exists.")
    else:
        # if account name is new, create the file with the given data
        with open(f"{acc_name}.txt", "w") as new_account:
            new_account.write("Account Name:\n")
            new_account.write(f"{acc_name}\n")

            new_account.write("Account Balance:\n")
            new_account.write(f"{initial_deposit}")

        print(f"Account {acc_name} created successfully.")
        print(f"Account Name: {acc_name}\nAccount Balance: {initial_deposit}")


def deposit(acc_name, amount):
    """
    Function to deposit amount to named account.
    Args:
        acc_name: <str>
        amount: <int>

    Returns:
        Success message if deposit is successful.

    """
    # open the account name in read default mode
    with open(f"{acc_name}.txt") as user_account:
        # create a list of the file contents
        user_info = user_account.readlines()

        if amount < 100:
            print("Minimum amount to deposit needs to be 100.")
        else:
            # pick out the value from the file content and edit it
            user_info[3] = str(int(user_info[3]) + amount)

            # open the file in write mode and join the contents list to a string in a new variable
            with open(f"{acc_name}.txt", "w") as updated_account:
                new_update = "".join(user_info)
                updated_account.write(new_update)
            print("Deposit Successful.")
            print("".join(user_info[2:]))
        # print(new_update)


def withdraw(acc_name, amount):
    """
    Function to withdraw amount from named account.
    Args:
        acc_name: <str>
        amount: <int>

    Returns:
        Success message if withdrawal is successful.

    """
    # open the account file in read mode
    with open(f"{acc_name}.txt") as user_account:
        user_info = user_account.readlines()
        user_total = int(user_info[3])
        if amount > user_total:
            print(f"You have insufficient funds to make a withdrawal.")
        else:
            user_info[3] = str(int(user_info[3]) - amount)
            with open(f"{acc_name}.txt", "w") as updated_account:
                new_balanace = "".join(user_info)
                updated_account.write(new_balanace)
                print("Withdrawal Successful.")
                print("".join(user_info[2:]))


# create_acc("kaya", 500)
# deposit("kaya", 10)
# withdraw("kaya", 1_000)

