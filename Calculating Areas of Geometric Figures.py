'''Experiment No:-2
   Title:-  Calculating Areas of Geometric Figures*
   Aim:-    Write a python program to calculate areas of any geometric figures
            like circle, rectangle and triangle.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                             '''
import math
def circle_area():
    """Calculate the area of a circle"""
    radius = float(input("Enter the radius of the circle:- "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f} square units\n")
def rectangle_area():
    """Calculate the area of a rectangle"""
    length = float(input("Enter the length of the rectangle:- "))
    width = float(input("Enter the width of the rectangle:- "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f} square units\n")
def triangle_area():
    """Calculate the area of a triangle"""
    base = float(input("Enter the base of the triangle:- "))
    height = float(input("Enter the height of the triangle:- "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f} square units\n")
def main():
    while True:
        print("\n Choose a geometric figure:- ")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Exit")
        choice = input("Enter your choice (1-4):- ")
        if choice == "1":
            circle_area()
        elif choice == "2":
            rectangle_area()
        elif choice == "3":
            triangle_area()
        elif choice == "4":
            print("Exiting the program. Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please select a valid option (1-4).")
# Start the program
main()

