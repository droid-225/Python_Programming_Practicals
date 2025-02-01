import numpy as np

# Create a NumPy array
array1 = np.array([1, 2, 3, 4, 5])
print("Array:", array1)

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:")
print(matrix)

# Basic operations
sum_array = np.sum(array1)
print("Sum of elements:", sum_array)

mean_value = np.mean(array1)
print("Mean of elements:", mean_value)

# Matrix operations
transpose_matrix = np.transpose(matrix)
print("Transpose of matrix:")
print(transpose_matrix)

# Dot product
dot_product = np.dot(matrix, transpose_matrix)
print("Dot product of matrix and its transpose:")
print(dot_product)

# Generate random numbers
random_array = np.random.rand(5)
print("Random array:", random_array)
