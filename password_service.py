import bcrypt

def get_user_record(username):
    """
    Loop through passwd file and retrieve the credential by username
    """
    try:
        with open("passwd.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                credential = line.split(":")
                if credential[0] == username:
                    return line
    except Exception as e:
        print(e)


def add_new_credential(username, password, role):
    is_user_existed = get_user_record(username)
    # If user not existed we append the new credential to file
    if not is_user_existed:
        # Encoding password
        encoded_password = password.encode('utf-8')
        # generating the salt with length 10
        salt = bcrypt.gensalt(10) 
        # Hashing the password 
        hash_password = bcrypt.hashpw(encoded_password, salt) 
        with open("passwd.txt", "a+") as file:
            file.write(f"{username}:{hash_password.decode('utf-8')}:{role}\n" )   
        return True
    
    return False

if __name__ == '__main__':
    print(add_new_credential("bobby", "password", "Regular_Client"))