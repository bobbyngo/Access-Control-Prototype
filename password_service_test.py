from password_service import *
import unittest

class TestPasswordFileMechanism(unittest.TestCase):
    def test_get_credential(self):
        credential = get_user_record("bobby")
        # Get the username by turning the record to the list and get first index
        actual = credential.split(":")[0]
        expected = "bobby"
        self.assertEqual(actual, expected) 

    def test_create_new_credential(self):
        self.assertTrue(add_new_credential("test_user", "ThisStrongCredent!al", "Regular_Client"))
        
        # Delete the test record immediately
        with open("passwd.txt", "r") as f:
            lines = f.readlines()
        with open("passwd.txt", "w") as f:
            for line in lines:
                if "test_user" not in line.strip("\n") :
                    f.write(line)

if __name__ == '__main__':
    unittest.main()