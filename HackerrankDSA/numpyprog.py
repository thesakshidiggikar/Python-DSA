# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n = input().strip()
arr = list(map(int, n.split()))
arr = np.array(arr)
print(np.reshape(arr, (3, 3)))
