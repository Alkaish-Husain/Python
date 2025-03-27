'''Post-lab :-2
   Title:-  Calculating Surface Areas of Geometric Figures*
   Aim:-    Write a program in python to find total surface area of cube and cuboid.  
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E. (Computer Engineering)
   Date:-                                '''
# Getting user input for cube dimensions
print("\n--- Calculate Surface Area of Cube ---")
side = float(input("Enter the side length of the cube: "))
# Calculating the surface area of the cube
cube_surface_area = 6 * (side ** 2)
print(f"Total Surface Area of Cube: {cube_surface_area} square units\n")
# Getting user input for cuboid dimensions
print("--- Calculate Surface Area of Cuboid ---")
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
# Calculating the surface area of the cuboid
cuboid_surface_area = 2 * (length * width + width * height + height * length)
print(f"Total Surface Area of Cuboid: {cuboid_surface_area} square units")
