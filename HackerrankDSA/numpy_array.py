import numpy as np
n, m = map(int, input().split())
array_data = []
for _ in range(n):
    row = list(map(int, input().split()))
    array_data.append(row)
arr = np.array(array_data)
transposed_arr = np.transpose(arr)
print(transposed_arr)
flattened_arr = arr.flatten()
print(flattened_arr)
