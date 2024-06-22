import numpy as np

n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
arr = np.array(arr)
a1 = np.mean(arr, axis=1)
a2 = np.var(arr, axis=0)
a3 = np.std(arr, axis=None)
print(a1)
print(a2)
print(np.around(a3, decimals=11))
