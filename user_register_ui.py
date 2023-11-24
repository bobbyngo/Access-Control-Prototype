from password_service import *
import stdiomask
import re 

def user_interface_prompt():
    """
    Interaction signup/signin prompt to get user input
    """
    print("-----------------------------------------\n" + \
    "Finvest Holdings\n" + \
    "Client Holdings and Information Systems\n" + \
    "-----------------------------------------")
    username = input("Enter username: ")
    password = stdiomask.getpass("Enter password: ")
    return username, password

def is_password_not_weak(password):
    # check if it's a weak password
    try:
        with open("weak_passwords.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if password == line.strip("\n"):
                    print("Weak password, Pick another one")
                    return False
    except Exception as e:
        print(e)
    return True

def is_password_valid(username, password):
    # Check if password contains username
    if username.lower() in password.lower():
        print("Password cannot have username")
        return False
    # Check if its having more than 8 characters
    if len(password) < 8:
        print("Password length must be at least 8 characters")
        return False
    special_charaters = "!@#$%?∗"
    # Check if its having uppercase
    if not any(char.isupper() for char in password):
        print("Password must have at least 1 upper case character")
        return False
    #Check if its having normalcase
    if not any(char.islower() for char in password):
        print("Password must have at least 1 lower case character")
        return False
    # Check if its having a number
    if not any(char.isdigit() for char in password):
        print("Password must have at least 1 number")
        return False
    # Check if its having a special character
    if not any(char in special_charaters for char in password):
        print("Password must have 1 special character")
        return False
    # Check if it matches to calendar pattern
    # 2023-09-23
    # 2018 12 21
    # 2818.01.19
    if re.search("[0-9][0-9][0-9][0-9](.|-|[ ]?)[0-9][0-9](.|-|[ ]?)[0-9][0-9]", password):
        print("Password cannot have a calendar pattern")
        return False
    # Check if it matches to licence plate pattern
    if re.search("[A-Za-z][A-Za-z][A-Za-z][A-Za-z](-|[ ]?)[0-9][0-9][0-9]", password):
        print("Password cannot have a licence plate pattern")
        return False
    # Check if it matches phone number pattern
    if re.search("[0-9][0-9][0-9](-|[ ]?)[0-9][0-9][0-9](-|[ ]?)[0-9][0-9][0-9][0-9]", password):
        print("Password cannot have a phone number pattern")
        return False
    return True


def register_user():
    credential = user_interface_prompt()
    if credential:
        username = credential[0]
        password = credential[1]
        existed = get_user_record(username)
        if existed:
            print("User has existed, try again")
        else:
            if is_password_not_weak(password) and is_password_valid(username, password):
                # default role to Regular Client
                add_new_credential(username=username, password=password, role="Regular_Client")
                print("Register user successful")

if __name__ == "__main__":
    while True:
        register_user()