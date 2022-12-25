import numpy as np

n = [6, 7, 8]
print(n[0: 2])
print(n[-1])

a = np.array([6, 7, 8])
print(a[0: 2])
a = np.array([
    [6, 7, 8],
    [1, 2, 3],
    [9, 3, 2]
])

print(a[0: 2, 2])  # elements of 2nd column (count from 0) of 0th and 1st row that is [8, 3]
print(a[-1, 0: 2])  # -1 is [9, 3 , 2] and 0: 2 in -1 gives [9, 3]
