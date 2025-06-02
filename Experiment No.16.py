'''Experiment No:-16
   Title:-  Script to Validate Phone Number and Email ID *
   Aim:-    Write a Python script that prompts the user to enter their phone number and email ID.
            It then employs Regular Expressions  to verify if these inputs adhere to standard
            phone number and email address formats
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                            '''
import re

def validate_phone_number(phone_number):
    phone_pattern = r"^\d{10}$"
    if re.match(phone_pattern , phone_number):
        return True
    else:
        return False

def validate_email(email):
    # Regular expression for validating the email format: name@eng.rizvi.edu.in
    # name can be alphanumeric (letters and digits)
    email_pattern = r"^[a-zA-Z0-9]+@eng\.rizvi\.edu\.in$"
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Get user input
phone_number = input("Enter your 10-digit phone number: ")
email = input("Enter your email ID (name@eng.rizvi.edu.in): ")

# Validate phone number
if validate_phone_number(phone_number):
    print("Phone number is valid.")
else:
    print("Phone number is invalid.")

# Validate email ID
if validate_email(email):
    print("Email ID is valid.")
else:
    print("Email ID is invalid.")
