'''Experiment No:-15
   Title:-  Using a Debugger*
   Aim:-    Demonstrate the use of a Python debugger (e.g., pdb or an IDE with debugging capabilities)
            on a sample program with intentional errors. 
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                            '''
import pdb

def divide_numbers(a, b):
    pdb.set_trace() # Set a breakpoint here to check the values of a and b
    result = a / b # This line will throw an error if b is zero
    return result

def calculate_average(numbers):
    pdb.set_trace() # Set a breakpoint here to inspect the numbers list
    total = sum(numbers) # This could throw an error if numbers is not a list
    return total / len(numbers)

def main():
    numbers = [10, 20, 30, 40, '50'] # Intentional error: one of the numbers is a string
    avg = calculate_average(numbers) # This will raise an error due to the string '50'
    print(f"The average is: {avg}")
    a, b = 10, 0 # Intentional division by zero error
    result = divide_numbers(a, b) # This will raise a ZeroDivisionError
    print(f"The result of division is: {result}")
    
if __name__ == '__main__':
    main()
