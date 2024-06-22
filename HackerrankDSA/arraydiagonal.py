import numpy as np

n, m = map(int, input().split())

ar1 = np.eye(
    n,
    m,
)
np.set_printoptions(legacy="1.13")
print(ar1)
