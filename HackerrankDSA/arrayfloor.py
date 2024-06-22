import numpy as np

A = input().split()
arr = np.array(A, dtype="float")
np.set_printoptions(legacy="1.13")
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
