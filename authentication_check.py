import bcrypt

def is_valid_credential(username, password):
        """
        Read all the lines in passwd.txt file to compare the credential
        If there is matched then access is granted
        """
        try:
            with open("passwd.txt", 'r') as file:
                lines = file.readlines()
                for line in lines:
                    credential = line.split(":")
                    if credential[0] == username \
                    and bcrypt.checkpw(password.encode('utf-8') , credential[1].encode('utf-8')):
                        return True
            
        except Exception as e:
            print(e)
        return False
           