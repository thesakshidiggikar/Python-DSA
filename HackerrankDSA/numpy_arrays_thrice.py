import numpy as np

# Read the dimensions n, m, p
n, m, p = map(int, input().split())

# Initialize two lists to hold the input data for both arrays
array_1_data = []
array_2_data = []

# Read the first array of dimensions n x p
for _ in range(n):
    row = list(map(int, input().split()))
    array_1_data.append(row)

# Read the second array of dimensions m x p
for _ in range(m):
    row = list(map(int, input().split()))
    array_2_data.append(row)

# Convert the lists to NumPy arrays
array_1 = np.array(array_1_data)
array_2 = np.array(array_2_data)

# Concatenate the arrays along axis 0
concatenated_array = np.concatenate((array_1, array_2), axis=0)

# Print the concatenated array
print(concatenated_array)
r