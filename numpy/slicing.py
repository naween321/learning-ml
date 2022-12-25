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

print("Iterating with np array")
for row in a:
    print(row)

for cell in a.flat:
    print(cell)

b = np.arange(6, 12).reshape(3, 2)
# print(np.vstack((a, b)))

b = a > 4
print(b)
print(a[b])

for x in np.nditer(a, order='C'):  # C refers to normal order
    print(x)

for x in np.nditer(a, order='F'):  # F refers to fortran order
    print(x)
