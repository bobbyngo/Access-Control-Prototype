import getpass
import stdiomask

class AuthInterface:
    
    
    def __init__(self):
        self.title ="Finvest Holdings\n" + \
                    "Client Holdings and Information Systems\n" + \
                    "-----------------------------------------"

    def get_user_credential(self):
        username = input("Enter username: ")
        password = stdiomask.getpass("Enter password: ")
        return username, password

    def is_valid_credential(self, username, password, credential_path):
        try:
            with open(credential_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line)
        except Exception:
            print(Exception)
        pass

    def display_user_access():
        pass

    def user_authentication(self):
        credential = self.get_user_credential()
        username = credential[0]
        password = credential[1]
        print(username + " " + password)

        self.is_valid_credential(username, password, "secrets/credentials.txt")

if __name__ == "__main__":
    auth = AuthInterface()
    print(auth.title)
    auth.user_authentication()
    