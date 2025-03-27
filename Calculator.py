'''Experiment No:-11
   Title:-  Simple Calcuator*
   Aim:-    Implement a simple Python calculator that takes user input and performs basic arithmetic
            operations (addition, subtraction, multiplication, division) using functions..
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                            '''
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        print("Enter the denominater greater than 0")
    return a / b
print("Simple Calculator")	
print("Choose An Option:-")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multilplication(*)")
print("4.Division(/)")
choice= input("Enter choice(1/2/3/4):- ")
num1 = float(input("Enter the first value:- "))
num2 = float(input("Enter the second value:- "))
if choice == "1":
    print(f"Result={add(num1,num2)}")
elif choice == "2":
    print(f"Result={sub(num1,num2)}")
elif choice == "3":
    print(f"Result={mul(num1,num2)}")
elif choice == "4":
    print(f"Result={div(num1,num2)}")
else:
    print("Invalid Choice! Please select choice from (1-4)")


