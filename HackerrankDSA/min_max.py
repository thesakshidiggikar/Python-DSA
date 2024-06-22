import numpy as np

N, M = map(int, input().split())

arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
arr = np.array(arr)
a1 = np.min(arr, axis=1)
print(np.max(a1))
