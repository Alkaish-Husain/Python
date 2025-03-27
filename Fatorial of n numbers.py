'''Experiment No:-9
   Title:-  Factorial Generator*
   Aim:-    Develop a Python program that takes a numerical(integer) input from the user and
            Calculating  the Factorial of N integer.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                           '''

n = int(input("Enter a Value:- "))
if n<0:
    print("Please a enter a positive integer")
else:
    result = 1
    for i in range(1,n+1):
        result*=i
    print(f"Factorial of {n} is {result}")





    
