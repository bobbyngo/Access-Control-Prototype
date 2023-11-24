from access_control_mechanism import *
from datetime import time
import unittest

class TestAccessControl(unittest.TestCase):
    def test_regular_client_access(self):
        actual = get_user_access("Regular_Client")
        expected = {
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R"],
            "Contact_Details_Financial_Advisor": ["R"]
        }
        self.assertEqual(actual, expected)

    def test_premium_client_access(self):
        actual = get_user_access("Premium_Client")
        expected = {
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R", "W"],
            "Contact_Details_Financial_Planner": ["R"],
            "Contact_Details_Investment_Analyst": ["R"],
        }
        self.assertEqual(actual, expected)

    def test_financial_planner_access(self):
        actual = get_user_access("Financial_Planner")
        expected = {
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R", "W"],
            "Money_Market_Instruments": ["R"],
            "Private_Consumer_Instruments": ["R"]
        }
        self.assertEqual(actual, expected)

    def test_financial_advisor_access(self):
        actual = get_user_access("Financial_Advisor")
        expected = {
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R", "W"],
            "Private_Consumer_Instruments": ["R"]
        }
        self.assertEqual(actual, expected)

    def test_investment_analyst_access(self):
        actual = get_user_access("Investment_Analyst")
        expected = {
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R", "W"],
            "Money_Market_Instruments": ["R"],
            "Derivatives_Trading": ["R"],
            "Interest_Instruments": ["R"],
            "Private_Consumer_Instruments": ["R"]
        }
        self.assertEqual(actual, expected)

    def test_teller_access_in_business_hour(self):
        actual = get_user_access("Teller", time(10,00))
        expected = {
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R"],
        }
        self.assertEqual(actual, expected)
    
    def test_teller_access_not_in_business_hour(self):
        actual = get_user_access("Teller", time=time(18,00))
        expected = "Teller can only access to system from 9:00am to 5:00pm"
        self.assertEqual(actual, expected)

    def test_compliance_officer_access(self):
        actual = get_user_access("Compliance_Officer")
        expected = {
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R"],
        }
        self.assertEqual(actual, expected)

    def test_technical_support_does_not_grant_access(self):
        actual = grant_access_to_technical_support("Regular_Client", False)
        expected = {
            "Client_Information": ["R"]
        }
        self.assertEqual(actual, expected)
    
    def test_technical_support_grant_access(self):
        actual = grant_access_to_technical_support("Regular_Client", True)
        expected = {
            "Client_Information": ["R"],
            "Account_Balance": ["R"],
            "Investments_Portfolio": ["R"],
            "Contact_Details_Financial_Advisor": ["R"]
        }
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()