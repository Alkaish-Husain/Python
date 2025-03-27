'''Experiment No:-3
   Title:-  Calculating Gross Salary of an Employee*
   Aim:-    Write a Python program to calculate the gross salary of an employee. The program
            should prompt the user for the basic salary (BS) and then compute the dearness allowance
            (DA) as 70% of BS, the travel allowance (TA) as 30% of BS, and the house rent allowance
            (HRA) as 10% of BS.Finally, it should calculate the gross salary as the sum of BS, DA, TA,
            and HRA and display the result.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                             '''
Basic_salary = float(input("Enter a Basic Salary:- "))
Dearness_Allowance = 0.70 * Basic_salary
print("Dearness_Allowance:- ",Dearness_Allowance)
Travel_Allowance = 0.30 * Basic_salary
print("Travel_Allowance:- ",Travel_Allowance)
House_Rent_Allowance = 0.10 * Basic_salary
print("House_Rent_Allowance:- ",House_Rent_Allowance)
Gross_Salary = Basic_salary + Dearness_Allowance + Travel_Allowance + House_Rent_Allowance
print("The Groos Salary is:- ",Gross_Salary)
