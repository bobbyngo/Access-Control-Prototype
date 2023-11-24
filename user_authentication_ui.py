import stdiomask
from access_control_mechanism import *
from authentication_check import *
from password_service import *

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

def user_sign_in():
    credential = user_interface_prompt()
    if credential:
        username = credential[0]
        password = credential[1]
    if is_valid_credential(username, password):
        print("ACCESS GRANTED!")
        # print all the access that the user has
        record = get_user_record(username).split(":")
        print("USERNAME: " + record[0])
        print("USER ROLE: " + record[2].strip("\n"))
        print("USER ACCESS:")
        print(get_user_access(role=record[2].strip("\n"), time=datetime.utcnow().time()))
    else:
        print("ACCESS DENIED!") 

if __name__ == "__main__":
    while True:
        user_sign_in()