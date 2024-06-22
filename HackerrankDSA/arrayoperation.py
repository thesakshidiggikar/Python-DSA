import numpy as np

# Read the dimensions
n, m = map(int, input().split())

# Read array A
A = np.array([input().split() for _ in range(n)], dtype=int)

# Read array B
B = np.array([input().split() for _ in range(n)], dtype=int)

# Perform operations
print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))  # Integer division
print(np.mod(A, B))
print(np.power(A, B))
