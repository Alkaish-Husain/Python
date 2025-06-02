'''Experiment No:-17
   Title:-  Extracting Data from Text *
   Aim:-    Create a program that reads a text file containing various data
            (e.g., names, emails, phone numbers).
            Use regular expressions to extract specific types of data,
            such as email addresses, phone  numbers,
            dates (e.g., MM/DD/YYYY format).
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                            '''
import re

# Function to extract data from the text
def extract_data_from_file(file_name):
    # Regular expressions for matching
    email_pattern = r"\b[a-zA-Z0-9._%+-]+@eng\.rizvi\.edu\.in\b"  # Improved email pattern
    phone_pattern = r"\b\d{10}\b"  # Matches a 10-digit phone number
    date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'  # Matches MM/DD/YYYY format

    # Read the file content
    with open(file_name, 'r') as file:
        text = file.read()

    # Extract emails, phone numbers, and dates
    emails = re.findall(email_pattern, text)
    phone_numbers = re.findall(phone_pattern, text)
    dates = re.findall(date_pattern, text)

    return emails, phone_numbers, dates

# Main function
def main():
    file_name = input("Enter the file name: ")

    try:
        # Extract data
        emails, phone_numbers, dates = extract_data_from_file(file_name)

        # Print the results
        print("\nExtracted Emails:")
        for email in emails:
            print(email)

        print("\nExtracted Phone Numbers:")
        for phone in phone_numbers:
            print(phone)

        print("\nExtracted Dates (MM/DD/YYYY):")
        for date in dates:
            print(date)

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
