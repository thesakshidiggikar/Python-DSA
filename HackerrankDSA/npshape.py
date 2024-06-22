import numpy as np

# Read the input shape
shape = tuple(map(int, input().split()))

# Create and print the array filled with zeros
zeros_array = np.zeros(shape, dtype=int)
print(zeros_array)

# Create and print the array filled with ones
ones_array = np.ones(shape, dtype=int)
print(ones_array)
