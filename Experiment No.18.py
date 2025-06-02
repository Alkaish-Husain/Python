'''Experiment No:-18
   Title:-  Creating and Manipulating Arrays*
   Aim:-    Write a Python program to create a 1D, 2D, and 3D NumPy array. Perform
            basic operations like reshaping, slicing, and indexing.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                            '''
import numpy as np
# 1D Array
print("1D Array:")
one_d_array = np.array([1, 2, 3, 4, 5])
print("Original 1D Array:", one_d_array)

# Indexing and Slicing 1D Array
print("Indexing 1D Array (Element at index 2):", one_d_array[2]) # Indexing

print("slicing 1D Array (Elements from index 1 to 3):", one_d_array[1:4]) # slicing
# Reshaping 1D Array to 2D
reshaped_2d = one_d_array.reshape(1, 5)
print("Reshaped 1D to 2D (1x5):", reshaped_2d)


# Indexing and slicing 2D Array
print("Element at (0, 2) in 2D Array: ", two_d_array[0, 2]) # Indexing
print("First row of the 2D Array: ", two_d_array[0]) # Row slicing
print("Elements from row 1, columns 1 to 2:", two_d_array[1, 1:3]) # Slicing

reshaped_3d = two_d_array.reshape(1,2,3)
print("Reshaped 2D to 3D (1x2x3):", reshaped_2d)

# 3D Array
print("\n3D Array:")
three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

 # 3D Array
print("\n3D Array:")
three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("Original 3D Array: \n", three_d_array)
# Indexing and slicing 3D Array
print("Element at (0, 1, 2) in 3D Array:", three_d_array[0, 1, 2]) # Indexing

 # Indexing and slicing 3D Array
print("Element at (0, 1, 2) in 3D Array:", three_d_array[0, 1, 2]) # Indexing

print("First 2D matrix of the 3D Array:\n", three_d_array[0]) # 2D slice
# Extracting elements from all layers, first row, second column

print("Elements from 3D Array (All layers, first row, second column):", three_d_array[:, 0, 1])

print("First 2D matrix of the 3D Array:\n", three_d_array[0]) # 2D slice
# Extracting elements from all layers, first row, second column
print("Elements from 3D Array (All layers, first row, second column):", three_d_array[:, 0, 1])

# Reshaping 3D Array to 2D
reshaped_2d_from_3d = three_d_array.reshape(2, 6)
print("Reshaped 3D to 2D (2x6):\n", reshaped_2d_from_3d)
