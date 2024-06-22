import numpy as np

# Read dimensions N and M
N, M = map(int, input().split())

# Initialize an empty list to store rows
arr = []

# Read N lines of input to populate the 2D array
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

# Convert the list of lists (rows) into a numpy array
arr = np.array(arr)

# Calculate the sum along axis 1 (columns)
sum_along_axis = np.sum(arr, axis=1)

# Calculate the product of the sums
product_of_sum = np.prod(sum_along_axis)

# Print the result
print(product_of_sum)
