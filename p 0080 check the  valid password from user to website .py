"""
A website requires the users to input username and password to register. Write a
program to check the validity of password input by users. Following are the criteria
for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria are to
be printed, each separated by a comma.

"""

import re       
def valid_password(password):
    if 6 <= len(password) >= 12 :
        if re.march(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])"):
            return True
    return False
password = input("Enter the password separated by commas : ").split(',')
valid_passwords = []
for psw in password:
    if valid_password(psw):
        valid_password.append(psw)

print(','.join(valid_password))
