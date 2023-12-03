# Access Control Prototype

### Description
A Python app that implement access control prototype using RBAC (Role-based access control) and Access Control Matrix. The passwd.txt is acting like a database

### Password policy

- Passwords must be least 8-12 characters in length
- Password must include at least:
  * one upper-case letter;
  * one lower-case letter;
  * one numerical digit, and
  * one special character from the set: {!, @, #, $, %, ?, ∗}
- Passwords found on a list of common weak passwords (e.g., Password1, Qwerty123, or Qaz123wsx) must be prohibited, which are stored in weak_passwords.txt
– Special Note: The list should be flexible to allow for the addition of new exclusions over time.
- Passwords matching the format of calendar dates, license plate numbers, telephone numbers, or other common numbers must be prohibited
- Passwords matching the user ID must be prohibited

### Access Control Policy
- Clients can view their account balance, view their investments portfolio, and view the contact details
of their Financial Advisor
- Premium Clients can modify their investment portfolio and view the contact details of their Financial
Planner and Investment Analyst
- All Finvest Holdings employees (except for Technical Support) can view a client’s account balance and
investment portfolio, but only Financial Advisors, Financial Planners, and Investment Analysts can
modify a client’s investment portfolio.
- Financial Planners can view money market instruments.
- Financial Advisors and Financial Planners can view private consumer instruments.
- Investment Analysts can view money market instruments, derivatives trading, interest instruments,
and private consumer instruments.
- Technical Support can view a client’s information and request client account access to troubleshoot
client’s technical issues.
- Tellers can only access the system during business hours from 9:00AM to 5:00PM.
- Compliance Officers can validate modifications to investment portfolios

### Registration
Navigate to user_register_ui.py and run the program to register. If the password doesn't match the policy, error will display </br>
![image](https://github.com/bobbyngo/Access-Control-Prototype/assets/76576373/cc7adebe-fa60-4bc0-a139-1016064a83da)
</br>
![image](https://github.com/bobbyngo/Access-Control-Prototype/assets/76576373/ff4ac052-64cb-4cdc-9f67-f838f75ce703)

### Authentication
Navigate to user_authentication_ui.py and run the program to authenticate. If authenticate successful, the user access rights will display </br>
![image](https://github.com/bobbyngo/Access-Control-Prototype/assets/76576373/2026efb7-1d61-4b76-91ae-6bd085893faa)
</br>
![image](https://github.com/bobbyngo/Access-Control-Prototype/assets/76576373/2a9fa0fc-b276-4ab8-a41c-b842260dbcd0)

