'''Experiment No:-10
   Title:-  Using function, write a Python program to analyze the input number is prime or not..
   Aim:-    Develop a Python program that takes a numerical input and identifies whether
            it is prime or not.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                  '''   
def is_prime(n):
    if n < 2:
         return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True     
n = int(input("Enter a number:- "))
if is_prime(n):
    print(f"Number {(n)} is prime")
else:
    print(f"Number {(n)} is not prime")
        
        
