'''Experiment No:-4
   Title:-  Exploring Basic Arithmetic Operations in Python*
   Aim:-    Write a Python program to explore basic arithmetic operations.
            The program should prompt the user to enter two numbers and then perform addition,
            subtraction, multiplication, division, and modulus operations on those numbers.
            The results of each operation should be displayed to the user.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                            '''
num1 = float(input("Enter a First Value:- "))
num2 = float(input("Enter a Second Value:- "))
# All operattions
Add = num1 + num2
Sub = num1 - num2
Mul = num1 * num2
# Check num2 is zero or not
if num2 == 0:
             print("Divide by Zero is not possible....")
             print("Second Zero is not possible in Modulus...")
else:
    div = num1 / num2
    mod = num1 % num2
print(f"{num1} + {num2} = {Add}")
print(f"{num1} - {num2} = {Sub}")
print(f"{num1} * {num2} = {Mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {mod}")
