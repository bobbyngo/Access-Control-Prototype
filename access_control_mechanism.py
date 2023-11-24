from datetime import datetime, time

authorization = {
    "Regular_Client" : {
        "Account_Balance": ["R"],
        "Investments_Portfolio": ["R"],
        "Contact_Details_Financial_Advisor": ["R"]
    },
    "Premium_Client": {
        "Account_Balance": ["R"],
        "Investments_Portfolio": ["R", "W"],
        "Contact_Details_Financial_Planner": ["R"],
        "Contact_Details_Investment_Analyst": ["R"],
    },
    "Financial_Planner": {
        "Account_Balance": ["R"],
        "Investments_Portfolio": ["R", "W"],
        "Money_Market_Instruments": ["R"],
        "Private_Consumer_Instruments": ["R"]
    },
    "Financial_Advisor": {
        "Account_Balance": ["R"],
        "Investments_Portfolio": ["R", "W"],
        "Private_Consumer_Instruments": ["R"]
    },
    "Investment_Analyst": {
        "Account_Balance": ["R"],
        "Investments_Portfolio": ["R", "W"],
        "Money_Market_Instruments": ["R"],
        "Derivatives_Trading": ["R"],
        "Interest_Instruments": ["R"],
        "Private_Consumer_Instruments": ["R"]
    },
    "Teller": {
        "Account_Balance": ["R"],
        "Investments_Portfolio": ["R"],
    },
    "Compliance_Officer": {
        "Account_Balance": ["R"],
        "Investments_Portfolio": ["R"],
    },
    "Technical_Support": {
        "Client_Information": ["R"]
    }
}

def get_user_access(role, time=None):
    if role == "Teller" and not is_business_hour(time):
        return "Teller can only access to system from 9:00am to 5:00pm"
    return authorization[role]

def is_business_hour(designated_time):
    designated_time = designated_time or datetime.utcnow().time()
    return designated_time >= time(9,00) and designated_time <= time(17,00)


def grant_access_to_technical_support(role, isGranted):
    if isGranted:
        user_access = get_user_access(role)
        authorization["Technical_Support"].update(user_access)
    return get_user_access("Technical_Support")
