'''Experiment No:-14
   Title:-  Basic Exception Handling*
   Aim:-    Python program that takes two numbers as input and performs division.
            Implement exception handling to manage division by zero and invalid input errors gracefully.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                            '''
def divide():
    try:
        num1 = float(input("Enter a First Number:- "))
        num2 = float(input("Enter a Second Number:- "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is :{result}")
    except ZeroDivisionError:
        print("Error:-Divide by Zero is not possible.")
divide()

        
   
          


